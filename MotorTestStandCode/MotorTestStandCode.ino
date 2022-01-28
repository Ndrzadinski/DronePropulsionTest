/*
 * Nathan Drzadinski
 * 10/26/2021
 * Motor Test Stand
 * 
 */

#include <HX711.h>
#include <Servo.h>

HX711 scale;

Servo ESC;

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 6;
const int LOADCELL_SCK_PIN = 7;

int error = 0; // Equals PWM jumps
int count = 0; // Equals num of trials at each speed
int x;
float calibration_factor = 111;
float units;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  ESC.attach(9);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  ESC.write(0);
  scale.set_scale(calibration_factor); //Adjust to this calibration factor
 scale.tare();  //Reset the scale to 0
}

void loop() {
  //Reads incoming Int and sets motor speed to correspond.
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (((x>=error)&(x<181))||x==0){
    ESC.write(x);
  }
  count++;
  units = scale.get_units(), 5;
 
  Serial.print(units);

  //Stops occasional bit error 
  if (count>10) {
    count = 0;
    error+=1; // Up by ten, must change to python step
  }
  //resets error at end of python code
  if (error > 180){
    error =0;
  }
}
