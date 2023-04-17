int sensor0 = 0;
int sensor1 = 0;
int sensormap0 = 0;
int sensormap1 = 0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  sensor0 = analogRead(A0);
  sensor1 = analogRead(A1);
  sensormap0 = map(sensor0, 0,1023 ,0,600);
  sensormap1 = map(sensor1, 0,1023 ,0,600);
  
  
  Serial.println(sensormap0+(String)" "+sensormap1);
  delay (1);
 
}
