Title: First Post - This Pelican Blog
slug: mypelicanblog
date: 2018-05-06
category: Blog
Tags: blog, python, pelican

When trying to figure out how to launch my first blog, I stumbled upon the vast options that are out there.  I realized that the Wordpress's and SquareSpace's that are out there were a little too modern, with some of their themes being a bit much.  I wanted something easy, but also something perhaps challenging that would help me learn a bit about the finer details of programming and web development.  Already in love with the Python programming language, I landed on [**this Pelican Tutorial**](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html) from [**Fullstackpython.com**](https://www.fullstackpython.com/).  

I followed that tutorial until the end and had to do a bit more digging on how to deploy to S3, including how to use with CloudFlare's SSL services.  Static sites like this one do not necessarily need HTTPS, but it's becoming _de rigure_ so I wanted to implement it anyway.  After some more extensive Googling (S3 + Pelican + CloudFlare) and a quick CloudFlare support ticket, I finally had it up and running.

