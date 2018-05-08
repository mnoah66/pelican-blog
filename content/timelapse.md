Title: Raspberry Pi Timelapse
slug: raspberrypi-timelapse
date: 2018-05-07
category: Blog
Tags: timelapse, ffmpeg, raspberrypi, python

# What can't the Pi Do?

The beauty of the Raspberry Pi is the millions of things you're able to do with it.  From a custom DIY webserver to a home surveillance system, from physical computing to the topic of this post: timelapse photography.  I became interested in the Raspberry Pi when it came time to purchase my home.  I wanted a DIY home surveillance system without exorbitant subscription costs or contracts, and the ability to fully customize it in any way I wanted.  .  I came across [**PyImageSearch**](https://pyimagesearch.com) and the amazing collection of tutorials ([this one in particular](https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/))

That was my introduction to the Raspberry Pi and it's camera module, and the timelapse idea came from a construction project next to my employer's office space.  Creating a timelapse with the Raspberry Pi is incredibly simple, and you don't need 100's of dollars worth of equipment. 

## Items Required

* [Raspberry Pi (duh!).  I purchase the kit which includes two heat sinks and the power supply](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=sr_1_3?s=pc&ie=UTF8&qid=1525737615&sr=1-3&keywords=raspberry+pi+3+b%2B&dpID=51IC7SDI3cL&preST=_SY300_QL70_&dpSrc=srch)
* [Raspberry Pi Camera](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?ie=UTF8&qid=1525737711&sr=8-3&keywords=pi+camera&dpID=41oaX6czzQL&preST=_SY300_QL70_&dpSrc=srch)

## Considerations

Once you have your Pi up and running and the camera tested and working, it's time to code your time lapse program.  Depending on your subject, you want to consider a few things before beginning your timelapse project.

1. **Frequency of pictures:** are you doing a time lapse of a 12 month construction project?  Snow melting and the leaves turning green? Or just some general foot traffic of humans in a park?  For each scenario, you need to decide how many pictures to take a [minute, hour, day, etc.].  [This](https://www.photopills.com/calculators/timelapse) timelapse calculator can help you decide how many pictures to take, considering also the filesize and length of your timelapse.  Be mindful of your audience, and that a two minute timelapse can have the same wow factor has a five minute one.
2. **File size and memory:** If you use generic settings with your camera and you only have an 8gb or 16gb SD card, you may run into storage issues if you take a lot of pictures.  For this project, I used a 128gb SD card, which had to be formatted in a particular way to work on the Raspberry Pi (https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md).
3. **Backups:** You may want to backup your images on an hourly/daily/weekly basis.  I've come across enough ocmments on the web about SD cards failing in the Raspberry Pi, and you certainly don't want a failure for something like this.  For this project, all images are saved locally to the SD card of the Pi, but also uploaded to my Dropbox account via the [Dropbox Python API](https://www.dropbox.com/developers/documentation/python).  Of course, a free plan may not give you enough memory, but I happily started paying for Dropbox (1TB) a few years ago and have _never_ regretted it.
4.  **Notification:** Will you be checking in with the progress of the timelapse every day?  If not, you may want to be notified when/if problems have occurred--mainly if the camera is taking pictures or not.  With Twilio SMS, you can add text message notification when the program has started and stopped taking pictures.  If on any given day you don't recieve the text, you'll know something's up and you should check things out.

### Setup

OK, so you've decided you want to take one picture every 30 minutes, only during day time hours.  Let's start with our Python code broken up into chunks here with some comments. The full code in its entirety is at the end.

```python
#!/usr/bin/python
# Camera.py
import datetime
import time
from picamera import PiCamera
import dropbox
from twilio.rest import Client
```

You'll need to install the dropbox and twilio modules with `pip install dropbox twilio` and import them accordingly. 

```python
twilio_id = "YOUR_TWILIO_ID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"

try:
  client = Client(twilio_id, twilio_auth_token)
  client.api.account.messages.create(
      to="+RECIPIENT",
      from_="+YOUR_TWILIO_NUMBER",
      body="Time Lapse has begun!")
except:
  pass
```

The above will send you a "Time Lapse has begun" text message at the beginning of the program.  This is a one time notification and we throw it in the try/except - pass block.  In case that piece doesn't work, it won't compromise the rest of your code.  If you don't plan to use the Twilio SMS notification, simply remove the entire lines above.  I believe Twilio gives you some free messages, but not sure of the limitations.

```python
camera = PiCamera()
```

Instantiate the PiCamera class and name it camera.

```python
start = time.time() 
PERIOD_OF_TIME = 43200 # Run this loop for 12 hours
```

Capture the time when the program began, then assign a variable equal to the total duration you want the progrm to run and take pictures, where 43200 seconds is equal to 12 hours (More on this later).

```python
dbx = dropbox.Dropbox("YOUR_SECRET_KEY")
```

Create your Dropbox object, replacing "YOUR_SECRET_KEY" with your own key.

And, finally-- the rest of the program:

```python
while True:
  timestr = time.strftime("%Y%m%d-%H%M%S")
  camera.resolution = (3280, 2464)
  #camera.hflip = True # If your camera is upside down
  #camera.vflip = True # If your camera is upside down
  time.sleep(2) # let the camera warm up
  camera.capture("/home/pi/TimeLapse/Pics/" + timestr + ".jpg")
  #Upload to dropbox
  try:
    dbx.files_upload(open("/home/pi/TimeLapse/Pics/" + timestr + ".jpg", "rb").read(), "/TimeLapse/" + timestr + ".jpg")
  except Exception as e:
    logf.write('The following error occurred on: ' + timestr + ': ' + str(e)+'\n')
    #pass
  time.sleep(1798)
  if time.time() > start + PERIOD_OF_TIME:
    client.api.account.messages.create(
    to="+RECIPIENT",
    from_="+YOUR_TWILIO_NUMBER",
    body="Finished taking pictures!")
    break
```

