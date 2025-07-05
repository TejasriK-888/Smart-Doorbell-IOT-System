#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4); 

int redLEDPin = 2;  // Digital pin for the red LED
int greenLEDPin = 3; // Digital pin for the green LED

void setup() {
  lcd.init();
  lcd.backlight();
  pinMode(redLEDPin, OUTPUT);
  pinMode(greenLEDPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Arduino will wait for commands from Python via Serial communication
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      openLock();  // If '0' is received, open the lock
    } else if (command == '0') {
      closeLock();  // If '1' is received, close the lock
    }
  }
}

void openLock() {
   
  digitalWrite(redLEDPin, LOW);  // Turn off the red LED
  digitalWrite(greenLEDPin, HIGH); // Turn on the green LED
  lcd.clear();
  lcd.setCursor(0, 1);
  lcd.print("Welcom Home"); //print message
  delay(1000);
  digitalWrite(redLEDPin, LOW);  // Turn off the red LED
  digitalWrite(greenLEDPin, LOW); // Turn off the green LED
  
}

void closeLock() {
  digitalWrite(redLEDPin, HIGH);  // Turn on the red LED
  digitalWrite(greenLEDPin, LOW); // Turn off the green LED
  lcd.clear();
  lcd.setCursor(0, 1);  
  lcd.print("stranger"); //print message
  delay(1000);
  digitalWrite(redLEDPin, LOW);  // Turn off the red LED
  digitalWrite(greenLEDPin, LOW); // Turn off the green LED
}
