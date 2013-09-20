from flask import Flask
from flask import request
import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

# oh god why
alpha = {'a':'12', 'b':'2111', 'c':'2121', 'd':'211', 'e':'1', 'f':'1121', 'g':'221',
         'h':'1111', 'i':'11', 'j':'1222', 'k':'212', 'l':'1211', 'm':'22', 'n':'21',
         'o':'222', 'p':'1221', 'q':'2212', 'r':'121', 's':'111', 't':'2', 'u':'112',
         'v':'1112', 'w':'122', 'x':'2112', 'y':'2122', 'z':'2211', '1':'12222',
         '2':'11222', '3':'11122', '4':'11112', '5':'11111', '6':'21111', '7':'22111',
         '8':'22211', '9':'22221', '0':'22222', ' ':' '}

app = Flask(__name__)

def on(duration):
    ser.write('1')
    ser.read()
    time.sleep(duration)
    ser.write('0')
    ser.read()

@app.route('/', methods=['POST'])
def write_out():
    body = request.form['Body'] # get SMS body
    print body
    for char in body:
        signals = alpha[char.lower()]
        for signal in signals:
            if signal == '1':
                on(0.2) # Send dot
            elif signal == '2':
                on(0.4) # Send dash
            time.sleep(0.2)

    # Return empty TwiML so Twilio doesn't complain
    return '<Response></Response>'

if __name__ == '__main__':
    app.run(debug=True)
