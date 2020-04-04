Title: Reminders with Python, Telegram and Pythonanywhere
slug: python-reminders-with-telegram
date: 2018-10-25
category: Blog
Tags: python, pythonanywhere, telegram
share_post:true
og_image:images/garbagetwittercard.png
Summary: Is today a recycling day?  A simple automated way to remind yourself.

## Is Today a Recyling Day?

Is what I ask myself every Wednesday morning.  On Wednesday's garbage is collected but every other week it's Garbage **and** Recyling day, but I can never remember and end up having to check the calendar on a website.  So inconvenient, right?!  Let's automate with Python and Telegram.  Telegram is a text messaging service kind of like WhatsApp but it's completely free, and they have an API for things just like this.  Head on over to [Telegram.org](https://telegram.org/) for more info.

What we want to accomplish is this: a Telegram bot to text me every Wednesday morning, indicating if it's a recycling and garbage day, or just garbage.  But how do I schedule a task to run every morning? This is a tricky task (sorry,&mdash;I had to) especially for beginners. Enter [PythonAnywhere](https://www.pythonanywhere.com), an incredible source for developing and programming with Python.  It offers full-blown Python environments and website hosting with your own subdomain, and a helpful blog and forum if you're just getting started.  One of it's cool features and a co-subject of this post are scheduled tasks, in which you can write a script to execute at a set time every day.

With the time this has saved me from having to manually check recycling calendars, I'm able to share how I did it with the world! 

## Are you ready?

We'll need the following:

1. A [Pythonanywhere.com](https://wwww.Pythonanywhere.com) account - a free account will work.
2. The Telegram app installed on your phone.
3. Pictures of garbage/recycling (optional).


## Telegram

Download the telegram app on your smartphone and start a chat with the @BotFather.  Create a new bot with the /newbot command, and the @BotFather will chat with you for the details.  He'll ask you for a general name for your bot and then a unique username. Once finished you'll be given an HTTP API token&mdash;keep that handy as we'll need it later.  

<img style="max-width: 400px;width:100%; height: 	auto;" src='/images/fatherbot.png'>

Back in the main chat menu of Telegram, create a new group.  Tap the search bar, and search for the username of your bot.  What you'll end up with is a "group" chat, but it's only yourself and your bot.  Now we need one additional credential before we can jump into the Python script, and it's the group chat ID. To get the ID, go to [https://web.telegram.org](https://web.telegram.org) and follow the steps to get into your account.  Once in, click the group chat you created with your bot.  In the address bar, you'll see a parameter that begins with the letter 'g'.  Take note of this ID.  If you get stuck obtaining the chat ID, [see this SO question and answers:](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id#answer-50661601)

<img style="max-width: 400px;width:100%; height: 	auto;" src='/images/chat_id.png'>

## The script

Let's start by writing the Python script, **garbage.py**
```
import telegram
from datetime import date

bot = telegram.Bot(token='YOUR_UNIQUE_TOKEN')

```
Import the necessary libraries and create our bot.  Remember to grab your own token that @BotFather gave you.

```
recycling_days = ['2018-01-10', '2018-01-24', '2018-02-07','2018-02-21', '2018-03-07', '2018-03-21',
                '2018-04-07', '2018-04-18', '2018-05-02', '2018-05-16', '2018-05-30', '2018-06-13',
                '2018-06-27', '2018-07-11', '2018-07-25', '2018-08-08', '2018-08-22', '2018-09-05',
                '2018-09-19', '2018-10-03', '2018-10-17', '2018-10-31', '2018-11-14', '2018-11-28',
                '2018-12-12', '2018-12-26']
```
Create a simple list of strings of the recyling days.

```
today = date.today()
```
Assign today's date to the variable `today`

```
if today.weekday() == 2:
    if str(today) in recycling_days:
        bot.send_photo(chat_id=-<YOUR_CHAT_ID>, photo=open('garbage_recycling.jpg', 'rb'))
        bot.send_message(chat_id=-<YOUR_CHAT_ID>, text="Recycling!")
    else:
        bot.send_photo(chat_id=-<YOUR_CHAT_ID>, photo=open('garbage.jpeg', 'rb'))
        bot.send_message(chat_id=-<YOUR_CHAT_ID>, text="Today is just a garbage day.")
```
**Note the '-' before your chat id** so an example would be `chat_id=-9999233`

Pythonanywhere's scheduled task feature will run every single day at the time you tell it to run.  For free accounts, you cannot specifiy what day you want it to run, or at what hour.  So we have to decide in our code what day of the week it is, since Garbage/Recycling days are only on Wednesdays (and we don't want to get a Telegram message every day).  We just evaluate if `today.weekday() == 2` where Monday is the first day of the week starting at 0, Tuesday = 1, Wednesday = 2, and so on.

The rest of the code checks to see if todays date (converted to a string) is in our list of `recycling_days`.  If it is, we send a photo of recycling cans and a message "Recyling!"  

<img style="max-width: 300px;width:100%; height:auto;" src='/images/recycleSmall.jpg'>

Otherwise, we send a garbage only image and message.

<img style="max-width: 300px;width:100%; height:auto;" src='/images/garbageSmall.jpg'>

## Pythonanywhere

Go to your Pythonanywhere account, navigate to the __Files__ tab and upload our file, **garbage.py**, and the images.  Then go to the __Consoles__ tab and under "Start a new console:" select **Bash**.

Once the terminal fires up, you'll need to install the Telegram python package.

In the console, type:
`pip3.6 install --user python-telegram-bot`

And, since the default Python version in Pythonanywhere is 2.7, you'll need to add a shebang on the first line of **garbage.py** so that Python 3.6 is used to run the script.

```python
#!/bin/env python3.6
import telegram

# The rest of the code...

```
### Tasks

Finally, navigate to the __Tasks__ tab of our Pythonanywhere account.  Under scheduled tasks, set the UTC time for when you want the script to execute.  I set mine for 10:00 which is 6:00AM NYC time and right around the time my recycling confusion sets in. 

In the command text box, enter `python 3.6 /home/YOUR_USERNAME/garbage.py` and create the task.

<img style="max-width: 800px;width:100%; height: 	auto;" src='/images/pythonanywhere_task.png'>

And now, wait and see if everything worked!



