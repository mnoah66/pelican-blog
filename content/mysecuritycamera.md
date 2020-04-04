Title: From Hobby to Criminal Evidence
slug: hobby-to-criminal-evidence-my-securiy-camera
date: 2018-05-20
category: Blog
Tags: surveillance, raspberrypi, python
og_image:images/burglary.jpg

We moved into our first home in May 2017 and by September we were victims of an attempted burglary.  We were one of the lucky ones that day; neighbors homes were broken into and items were stolen, including a diamond engagement ring.

It was late September 2017 and I am at my office when my wife calls, distraught, with the news that our neighbors home had been broken in to.  Items were stolen, and police were in the neighborhood checking nearby homes and speaking with residents.  Our home looked fine and there were no signs of intrusion or disturbance. Aside from the initial shock-and-awe of the news, we carried on about our day.  I finished up at the office and headed to the dentist to get stitches removed from a recent extraction (fun!).

When we moved in that spring, I purchased a Raspberry Pi and set up a surveillance system inspired by Adrian Rosebrock's [pyimagesearch](https://www.pyimagesearch.com/) and more specifically [this tutorial](https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/), so that any time there was motion detected inside my home, the Pi takes a picture and uploads it to my Dropbox account.  As I'm driving to the dentist, the thought of checking the Pi's surveillance photos flushes my body.  I pull over, open the Dropbox app and navigate to the photos from earlier on that day and see the usual photos of our lab, Athena, moving about and setting off the motion detection.  Sifting through the photos I see nothing unusual: there are no humans in my living room, and Athena looks relatively at-ease.  That is until I come across a picture where her tail is sticking straight out/up, and she is posturing towards the back of the house (she usually barks at activity in the front).  I scroll through two more pictures and my heart stops: a person at my back door.

<img style="max-width: 400px;width:100%; height: 	auto;" src='/images/burglary.jpg'>

Our door was locked, and Athena does not take kindly to strangers; she likely charged the door soon after this photo was taken, hair sticking up down her spine, barking deeply and loud.  Some officers came to our home and checked out the inside and outside and eventually took our information, including an email wth the image above.  A couple of months later, a press release indicated he was arrested and charged an assortment of offenses, including his attempted burlgary of our home.

I never expected my Raspberry Pi's home surveillance program to actually capture criminal activity as was evidenced in how little attention I paid to it.  At that time, I barely had the Pi up and running every day and cycled through various automation options, from cron jobs to a script that pinged the network to see if our cell phones were connected.  If not, the surveillance program would turn on.  We were mostly happy that we could check in on Athena and see what she is up to while we're away.

If you're comtemplating using a Raspberry Pi or a similar device as a home surveillance system, consider that it may not be as reliable as commercial devices and systems.  Consider that it doesn't have a 24x7 monitoring service that home security systems do and consider that it's reliability is 100% dependant on your knowledge and discipline.  Had I not made sure the system was working that day, I would never have known what happened (and maybe for the better).
