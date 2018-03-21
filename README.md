# SnapReview

A Shopify plugin to display video reviews.

## Current main objectives

### Fill out site content

We need a site for clients to learn about our product and their customers to record video.

### Get site to secure protocol (https)

Most browsers won't let us capture webcam input unless we use https.

We need to generate a security key and purchase an SSL certificate.

### Compile captured video into a compressed file

We currently have a way to capture video and spit it right back into the browser, but we really need to be compiling it into a file that can go in object storage.

We don't want to sacrifice quality but the videos should be reasonably compressed so we don't overpay for storage.
