#include "Arduino.h"
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() { 
  Serial.begin(9600);
  lcd.begin(16, 2); 
  
}

void loop() { 
  int sensorValue = analogRead(A1);
  double voltage = (3.3*sensorValue/666);
  double a = -6.2462641e-06, b= 2.9393882e-3,c=2.3348339;
  double Temp = (-b+sqrt(b*b - 4*a*(c-voltage)))/(2*a);
  Serial.println(Temp);
  Serial.println(voltage);
  lcd.print("Temp(in Celsius)");
  //lcd.setCursor(0,1);
  //lcd.print(voltage,2);
  lcd.setCursor(5,1);
  lcd.print(Temp,2);
  delay(500);
  lcd.clear();
}
