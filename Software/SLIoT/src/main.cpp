#include <Arduino.h>

const int micPin = 34; // Analog pin connected to MAX4466 OUT

void setup() {
    Serial.begin(115200); // Initialize Serial Monitor
    pinMode(micPin, INPUT); // Set the analog pin as input
}

void loop() {
    int micValue = analogRead(micPin); // Read the analog signal
    Serial.println(micValue);         // Send the reading to Serial
    delay(1);                         // Short delay for fast sampling
}
