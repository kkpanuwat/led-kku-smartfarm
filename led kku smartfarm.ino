#include <TimeLib.h>
int pin = 9;
void setup() {
  pinMode(pin, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println();
  setTime(23, 59, 50, 24, 5, 2021);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalClockDisplay();
  if (hour() == 23 && minute() == 59 && second() == 55) {
    digitalWrite(pin, HIGH);
  }
  if (hour() == 0 && minute() == 0 && second() == 0) {
    digitalWrite(pin, LOW);
  }
  delay(1000);
}

void digitalClockDisplay() {
  // digital clock display of the time
  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.print(" ");
  Serial.print(day());
  Serial.print(" ");
  Serial.print(month());
  Serial.print(" ");
  Serial.print(year());
  Serial.println();
}

void printDigits(int digits) {
  // utility function for digital clock display: prints preceding colon and leading 0
  Serial.print(":");
  if (digits < 10)
    Serial.print('0');
  Serial.print(digits);
}