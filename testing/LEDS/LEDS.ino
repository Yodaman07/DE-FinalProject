void setup() {
  // put your setup code here, to run once:
  
  pinMode(LED_GREEN, OUTPUT);
  
}

void loop() {
  
  digitalWrite(LED_GREEN, HIGH);


  delay(1000);
  digitalWrite(LED_GREEN, LOW);
  

  delay(1000);
  digitalWrite(LED_GREEN, HIGH);
  delay(1000);
}