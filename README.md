Beeper
=============

This was part of The Hacker Olympics at TwilioCon 13.

The goal:

> Check out an Arduino Uno and a USB cable from the registration desk.
Use the Twilio API and your Arduino in order to build a system that receives
incoming SMS messages and blinks them out in Morse code on your Arduino
using the built-in LED.

## Arduino

First, get [the arduino IDE](http://arduino.cc/en/main/software).
Take a second to silently complain with me about its lack of support
for deleting over spaced tabs.

Done? Great. You can go ahead and run the arduino.ino script from this
repository onto your Arduino board. Your Arduino will wait patiently
until it gets input.

## pySerial

Next install [pySerial](http://pyserial.sourceforge.net/).
```bash
$ pip install pyserial
```
This is how we will communicate with our Arduino board using python. In my
app.py, I have the following line that specifies which USB port on the
computer to talk to and which baud rate to use.

    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

You might need to change this so pySerial is able to connect to your arduino.

## ngrok

Now we will set up [ngrok](https://ngrok.com/). Ngrok is a magical service that
routes external URLs to a port on your local machine. Go to that link and set up
your account to point to port 5000 on your computer. Port 5000 is the port Flask
will run on.

## Flask

Speaking of [Flask](http://flask.pocoo.org/), go ahead and:
```bash
$ pip install flask
```
Flask is a simple python web framework. If you don't know how it works,
[you should](http://flask.pocoo.org/docs/).

Then just `cd` to this repo and:
```bash
$ python app.py
```

This will run your Flask app. It is now listening for `POST` requests to your ngrok URL
containing a `Body` parameter.

## Twilio

Next you'll need to set up everything Twilio related. Twilio will route the SMS to your
URL with the `Body` parameter set as the body of that text message. Amazeballs.
If you don't have an account, [get one](http://twilio.com).
Twilio is awesome and will make you a better human.

Go to your [Twilio Numbers page](https://www.twilio.com/user/account/phone-numbers/incoming).
Click on the number you wish to use. Set the "Messaging Request URL" to your ngrok url.

## MORSE CODE

Now, just text your Twilio number! If you set everything up correctly, your Arduino
should send the text message body to you over morse using its LED.

## Finishing up

That's it. You're awesome. If you thought this was cool follow me on
[twitter](http://twitter.com/dougblackio).
