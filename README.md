# Thai Sizzle

Website for **Thai Sizzle**, a Thai food truck at the Mabank Food Truck Park (207 E Market St, Mabank, TX). A restaurant is planned.

Built with [Jekyll](https://jekyllrb.com/) and deployed to GitHub Pages by GitHub Actions on every push to `main`.

## Updating the site

Most changes are a one-file edit. No coding is needed:

| What | File |
| --- | --- |
| Menu items, descriptions, prices | `_data/menu.yml` |
| Hours | `_data/hours.yml` |
| Featured reviews (hand-picked, word-for-word) | `_data/reviews.yml` |
| Google star rating and review count | `_data/google.yml` (auto-refreshed weekly) |
| Home page slideshow photos (order + captions) | `_data/gallery.yml` and `assets/images/food/` |
| Phone, address, Squarespace order link, Facebook | `_config.yml` → `business:` |
| "Restaurant coming soon" banner | `_config.yml` → `restaurant_teaser:` |
| About page text | `about.md` |

### Online ordering (Squarespace)
Payments and online orders go through Squarespace. Put the Squarespace ordering/checkout URL in `_config.yml`:

```yaml
business:
  order_url: "https://your-squarespace-site.com/order"
```

Every "Call to Order" button then becomes "Order Online". If you leave it blank, the buttons dial the phone number.

### Google reviews
The site shows the Google rating badge and hand-picked 5-star reviews. The rating and review count update every Monday through `.github/workflows/google-reviews.yml`:

1. In Google Cloud, enable **Places API (New)** and create an API key. Restrict the key to that API.
2. In the GitHub repo, go to **Settings → Secrets and variables → Actions** and add the secret `GOOGLE_PLACES_API_KEY`.
3. Run the workflow once from the **Actions** tab. It finds the Google place ID, fills in `_data/google.yml` and turns "Leave us a review" into a direct review link.

The key stays secret because it is only used at build time. It never reaches visitors. Usage is a few requests a week, which is well within Google's free tier.

### Photos
Photos are in `assets/images/food/` as WebP files in two sizes: `name.webp` (1200px) and `name-sm.webp` (640px). To add a dish photo, add both files and set `photo: name` on the item in `_data/menu.yml`.

### When the restaurant opens
1. In `_config.yml`, set `business.type: restaurant`. Structured data then switches to `Restaurant`.
2. Update the address, `location_name`, `lat`/`lng` and hours.
3. Set `restaurant_teaser.enabled: false`, or rewrite it as a grand-opening note.

### Custom domain
Add the domain under the repo's **Settings → Pages**, then set `url:` to the domain and `baseurl: ""` in `_config.yml`.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/thai-sizzle/.
