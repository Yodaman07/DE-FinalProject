#include "USB.h"
#include "USBHIDKeyboard.h"
USBHIDKeyboard Keyboard;

void setup() {
  // put your setup code here, to run once:
  Keyboard.begin();
  USB.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  
}
