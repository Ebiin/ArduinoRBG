const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;
String inData;


void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {

//Serial.println("vittuuuu");

          
          while (Serial.available() > 0) {
            /*
        
            char received = Serial.read();
            inData += received;
        
            if(received == '\n')<
            {
              Serial.print(inData);
            }
          
            inData = "";
        */

    int red = Serial.parseInt();
    int green = Serial.parseInt();
    int blue = Serial.parseInt();

    if (Serial.read() == 'x') {
      red = 255 - constrain(red, 0, 255);
      green = 255 - constrain(green, 0, 255);
      blue = 255 - constrain(blue, 0, 255);

      analogWrite(redPin, red);
      analogWrite(greenPin, green);
      analogWrite(bluePin, blue);
      
      Serial.print(red, HEX);
      Serial.print(green, HEX);
      Serial.println(blue, HEX);
    } 
  }
  
}
