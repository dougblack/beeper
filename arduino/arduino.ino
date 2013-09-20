int incomingByte = 0;
int pin = 13;

void setup() {
  Serial.begin(9600); // use port 9600
  pinMode(pin, OUTPUT); // use pin 13
}

void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.read(); // read byte

    if (incomingByte == '1') {
      digitalWrite(pin, HIGH);
      Serial.write('1'); // accept signal
    } else if (incomingByte == '0') {
      digitalWrite(pin, LOW);
      Serial.write('1'); // accept signal
    }

  } 
}
