#include "thingProperties.h"
#include "USB.h"
#include "USBHIDMouse.h"



USBHIDMouse Mouse;


bool movementActive = false;
void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500);

  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information you’ll get.
     The default is 0 (only errors).
     Maximum is 4
 */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();

  USB.begin();
  Mouse.begin();
}

void loop() {
  ArduinoCloud.update();
  // Your code here

  // put your main code here, to run repeatedly:
  if ((mouseX != -1) && (mouseY !=-1) ){
      // Serial.print(mouseX);
      // Serial.print(" and ");
      // Serial.print(mouseY);
      // Serial.print(" ; ");
      // Serial.println(movementActive);
      Mouse.move(mouseX, mouseY);
      movementActive = true;
  }else{movementActive = false;}

  if (!movementActive){scanForOpperations(mouseState);} //Listening for other mouse signals if movement isn't active

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

/*
  Since MouseX is READ_WRITE variable, onMouseXChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onMouseXChange()  {
  // Add your code here to act upon MouseX change
}


/*
  Since MouseY is READ_WRITE variable, onMouseYChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onMouseYChange()  {
  // Add your code here to act upon MouseY change
}

/*
  Since MouseState is READ_WRITE variable, onMouseStateChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onMouseStateChange()  {
  // Add your code here to act upon MouseState change
}
