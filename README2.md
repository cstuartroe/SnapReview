# SnapReview

A Shopify plugin to display video reviews.

## Current main objectives

### Authorization on Shopify as a partner

https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token

Set up as a public app (OAuth)

### Storage of video on AWS S3

We already have a short file that captures webcam input and displays it in real time.

We need to send it to an AWS bucket.

### Fill out site content

We need a site for clients to learn about our product and their customers to record video.

### Get site to secure protocol (https)

Most browsers won't let us capture webcam input unless we use https. idek how tf to do that with heroku but let's find out.
