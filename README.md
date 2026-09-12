# sparecms

***"spare": ... 3: not liberal or profuse ...***
***- Merriam-Webster***

**sparecms** is a CMS (content management system) for static sites that does *not* aim to be an all-inclusive CMS solution. It was born out of frustration with a number of other open source CMS systems that were too complicated, poorly documented, or limited in such a way as to push potential users to paid support options.

## Pre-Alpha Project

**sparecms** is in **absolutely pre-alpha state**. This is not production-ready software by any means. In fact, as of writing this readme file, it doesn't even really run - I'm still getting set up. I had the idea for this like two days ago. You probably shouldn't use it yet!

## Features

There's not many of them. That's the way I like it.

By design, sparecms does not automatically publish or deploy material, support a wide variety of static site generators, or do anything outside of the bare minimum of:
- authenticating users,
- enabling users to write, edit and manage articles,
- writing articles to disk in Markdown format,
- managing static content (images and the like) for said articles, and,
- turning those articles into a static site via [Pelican](https://getpelican.com/), if you want
    - You don't *have* to, but I 'm designing how content is stored to work nicely with Pelican.

Other CMSes may let you do things like automatically deploy to Cloudflare Pages or a S3 bucket, support a bunch of static site generators, or any number of other fun features.

This project's viewpoint on this kind of functionality is: rather than spend a lot of time supporting a wide variety of functionality, sparecms is going to focus on doing one thing well and leave the rest of it up to you. If you can install and configure sparecms, you can probably write a script of some kind to automatically sync the files to a Git repository, upload them to a host or CDN, or do whatever else you want to do with them.