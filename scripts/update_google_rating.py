"""Refresh _data/google.yml with the live Google rating and review count.

Uses the Google Places API (New). Needs the GOOGLE_PLACES_API_KEY env var.
If place_id is blank in _data/google.yml, it is looked up once by text search.
Standard library only, so the GitHub Action needs no pip installs.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

DATA = os.path.join(os.path.dirname(__file__), "..", "_data", "google.yml")
QUERY = "Thai Sizzle 207 E Market St Mabank TX"
KEY = os.environ.get("GOOGLE_PLACES_API_KEY")


def call(url, fields, body=None):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode() if body else None,
        method="POST" if body else "GET",
        headers={
            "X-Goog-Api-Key": KEY,
            "X-Goog-FieldMask": fields,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def set_field(text, key, value):
    """Replace the value of a top-level YAML key, keeping any trailing comment."""
    return re.sub(rf"(?m)^{key}:[^\n#]*?(\s*#.*)?$",
                  lambda m: f"{key}: {value}{m.group(1) or ''}", text, count=1)


def main():
    if not KEY:
        print("GOOGLE_PLACES_API_KEY not set; skipping.")
        return 0
    text = open(DATA, encoding="utf8").read()
    m = re.search(r'(?m)^place_id:\s*"?([^"\s#]*)', text)
    place_id = m.group(1) if m else ""
    if not place_id:
        res = call("https://places.googleapis.com/v1/places:searchText",
                   "places.id,places.displayName", {"textQuery": QUERY})
        place_id = res["places"][0]["id"]
        print("Resolved place id:", place_id, res["places"][0]["displayName"])
    place = call(f"https://places.googleapis.com/v1/places/{place_id}", "rating,userRatingCount")
    rating, count = place.get("rating"), place.get("userRatingCount")
    if rating is None or count is None:
        print("No rating returned; leaving file unchanged.")
        return 0
    text = set_field(text, "rating", rating)
    text = set_field(text, "review_count", count)
    text = set_field(text, "place_id", f'"{place_id}"')
    text = set_field(text, "updated", datetime.date.today().isoformat())
    open(DATA, "w", encoding="utf8").write(text)
    print(f"Rating {rating} from {count} reviews")
    return 0


if __name__ == "__main__":
    sys.exit(main())
