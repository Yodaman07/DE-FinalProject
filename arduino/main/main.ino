#include <Mouse.h>


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600) //9600 bits/second
}
//Testing code, implement with serial port data from the pi

void loop() {
  // put your main code here, to run repeatedly:
  String data = "";
  if (Serial.available() > 0){
      data = Serial.readString();
  }
  
  switch (data){

    case "10":
      Mouse.begin();
      Mouse.move(100, 0)
      Mouse.end();
      break;
    case "11":
      break;
    case "20":
      break;
    case "21":
      break;
    case "30":
      break;
    case "31":
      break;
  }
}

String parse(){
  return " ";
}
