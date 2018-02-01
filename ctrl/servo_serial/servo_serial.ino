#include <Servo.h>

Servo pan_servo;
Servo tilt_servo;
long pan_ang;
long tilt_ang;
int input_counter;

void setup() {
  // put your setup code here, to run once:
  pan_ang = 90;
  pan_servo.attach(10); // servo 1 on motor shield
  tilt_ang = 45;
  tilt_servo.attach(9); // servo 2 on motor shield
  Serial.begin(9600);
  pan_servo.write(pan_ang);
  tilt_servo.write(tilt_ang);
  Serial.print("Please enter pan and then tilt angle.");

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    if (input_counter == 0){
      pan_ang = Serial.parseInt();
      input_counter = input_counter + 1; 
      Serial.print(pan_ang);
      Serial.println(" degs");
      Serial.println("now enter tilt angle");
    }
    else if (input_counter == 1){
      input_counter = 0;
      tilt_ang = Serial.parseInt();
      Serial.print(tilt_ang);
      Serial.println(" degs");

      pan_servo.write(pan_ang);
      tilt_servo.write(tilt_ang);
      Serial.print("Please enter next pan and tilt angles");
    }
  } 
}
