#include "USB.h"
#include "USBHIDKeyboard.h"
USBHIDKeyboard Keyboard;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Keyboard.begin();
  // USB.begin();
  pinMode(LED_GREEN, OUTPUT);
}

void loop() {
  digitalWrite(LED_GREEN, LOW);
  // put your main code here, to run repeatedly:


  String data = "";
  if (Serial.available() > 0){
      data = Serial.readString();
  }

  if (data != ""){
    // Keyboard.print(data);
    digitalWrite(LED_GREEN, HIGH);
    delay(5000);
  }
}
