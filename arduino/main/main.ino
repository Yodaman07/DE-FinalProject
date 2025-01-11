#include "USB.h"
#include "USBHIDMouse.h"
USBHIDMouse Mouse;

bool movementActive = false;
int activeReadingState = 1; // 1 is x coord, 2 is y coord
int coords[] = {0, 0};

void setup() {
  // put your setup code here, to run once:
  USB.begin();
  Mouse.begin();
  Serial.begin(9600); //9600 bits/second
  
}
//Testing code, implement with serial port data from the pi

void loop() {
  
  // put your main code here, to run repeatedly:
  String data = "";
  if (Serial.available() > 0){
      data = Serial.readString();
  }
  int intData = data.toInt();

  switch (intData){
     case 123456788:
      //Start Mouse Movement: All subsequent values will alternate between x and y values
      movementActive = true;
      break;
    case 123456789:
      //End Mouse Movement: All other values will be read as mouse presses
      movementActive = false;
      break;
  }

  if ((data != "") && (movementActive)){
    if (activeReadingState == 1){coords[0] = intData;} //update x val
    if (activeReadingState == 2){coords[1] = intData;} // update y val

    activeReadingState++;

    if (activeReadingState==2){
      Mouse.move(coords[0],coords[1]);
      activeReadingState = 1;
    }
  }
  
  if (!movementActive){scanForOpperations(intData);} //Listening for other mouse signals if movement isn't active
  
}

void scanForOpperations(int data){
  switch (data){
      case 10:
        Mouse.press(MOUSE_MIDDLE);
        break;
      case 11:
        Mouse.release(MOUSE_MIDDLE);
        break;
      case 20:
        Mouse.press(MOUSE_LEFT);
        break;
      case 21:
        Mouse.release(MOUSE_LEFT);
        break;
      case 30:
        Mouse.press(MOUSE_RIGHT);
        break;
      case 31:
        Mouse.release(MOUSE_RIGHT);
        break;
      case 404:
        Mouse.end();
        break;
    }
}

