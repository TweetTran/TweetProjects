// C++ code
//
// declare spin directions, power and spin time variables
const int clockwise = 11;
const int counterClockwise = 6;
const int button = 4;
const long minTime = 1000;
const long maxTime= 60000;

void setup()
{
  pinMode (button, INPUT); // Initialize power button as input
  pinMode(clockwise, OUTPUT);  // initialize pin as an output
  pinMode(counterClockwise, OUTPUT);// initialize pin as another output
  Serial.begin(9600); // terminal output 
  
  randomSeed(analogRead(0)); // add randon seed to generate random selection
}

void loop() { 
  int direction = random(1, 3);       // Randomize direction of the motor (1 or 2)
  long duration = random(minTime, maxTime); // Randomize the time between 1 second and 1 minute
  int randomSpeed = random(10, 255); // Randomize the speed between 10 to full duty cycle
  
  // Clockwise direction
  if (direction == 1) { 
    digitalWrite(clockwise, HIGH);        // Activate the clockwise spin direction 
    digitalWrite(counterClockwise, LOW); // Ensure counter-clockwise is off
    analogWrite(clockwise, randomSpeed); // Apply PWM to control speed 
    delay(duration);                     // Spin for the randomized duration 
    Serial.print("Direction: Clockwise, Speed: ");
    Serial.print(randomSpeed);
    Serial.print(", Duration: ");
    Serial.println(duration);
  } 
  // Counter-clockwise direction
  else {
    digitalWrite(clockwise, LOW);        // Ensure clockwise is off
    digitalWrite(counterClockwise, HIGH); // Activate the counter-clockwise spin direction 
    analogWrite(counterClockwise, randomSpeed); // Apply PWM to control speed
    delay(duration);                     // Spin for the randomized duration 
    Serial.print("Direction: Counter-Clockwise, Speed: ");
    Serial.print(randomSpeed);
    Serial.print(", Duration: ");
    Serial.println(duration);
  }
  
  // Reset the motor after spinning
  digitalWrite(clockwise, LOW); 
  digitalWrite(counterClockwise, LOW);
  delay(300); // Pause for a third of a second before the next spin
  Serial.println("RESET");
}