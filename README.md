# Thai Sizzle

Website for **Thai Sizzle**, a Thai food truck at the Mabank Food Truck Park (207 E Market St, Mabank, TX). A restaurant is planned.

Built with [Jekyll](https://jekyllrb.com/) and deployed to GitHub Pages by GitHub Actions on every push to `main`.

## Updating the site

Most changes are a one-file edit. No coding is needed:

| What | File |
| --- | --- |
| Menu items, descriptions, prices | `_data/menu.yml` |
| Hours | `_data/hours.yml` |
| Customer quotes | `_data/reviews.yml` |
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
