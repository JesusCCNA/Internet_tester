#include "pitches.h"
 
int duration = 500;  // 500 miliseconds
 
void setup() {
 
}
 
void loop() {  
    // pin8 output the voice, every scale is 0.5 sencond
    tone(8, 200, duration);
    // Output the voice after several minutes
    delay(1000);
  
   
  // restart after two seconds 
  delay(1000);
}
