// Serial test script
#include <LiquidCrystal.h>
int setPoint = 55;
String readString;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps
  lcd.begin(16, 2);
}
char c;
void loop()
{
  
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }
  Serial.flush();
  if (readString.length() >1)
  {
    lcd.clear();
    lcd.print("ACC: ");  
    lcd.print(" ");
    lcd.print(readString); //see what was received
    
  }
  readString=" ";
  delay(500);
}
