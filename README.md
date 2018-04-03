# SnapReview

A Shopify plugin to display video reviews.

## Current main objectives

### Fill out site content

We need a site for clients to learn about our product and their customers to record video.

### Add audio

JS is capturing video for us. We need audio too unless all our reviews are going to be in sign language.

### Compile captured video into file I/O

We currently have a way to capture video and spit it right back into the browser, but we really need to be compiling it into a file I/O that can go in object storage.

### Spaces API and file pipeline

Once Javascript has some kind of file-like object with our video capture, we need to load a bitstream into a DigitalOcean Space via their API. We'll probably need to build a pipeline that involves some amount of video compression.

https://developers.digitalocean.com/documentation/spaces/

### Database

Our current concept is that we'll have a SQL database on the Django site that has entries for video objects with their associated store, product, timestamp, video file code, and potentially things like ratings and the status of approval from the vendor (pending, rejected, accepted). When videos are uploaded, they'll be sent to a Space and given a unique alphanumeric code, and then we'll use our SQL database to find the files associated with a store or product.

So we need to set up the database models in Django and build a lil API to add and request videos.

### Try using Shopify API

In theory we have a working OAuth setup with Shopify but we haven't actually tested it by making any Shopify API calls. Maybe for now we should just try a baby API call to make sure we can talk to Shopify at all.

https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token
