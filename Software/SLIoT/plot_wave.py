import serial
import matplotlib.pyplot as plt
from collections import deque

 
ser = serial.Serial('COM11', 115200) 
plt.ion()  # Interactive mode for real-time plotting

# Buffer to store incoming data
BUFFER_SIZE = 500
data_buffer = deque([0] * BUFFER_SIZE, maxlen=BUFFER_SIZE)

fig, ax = plt.subplots()
line, = ax.plot(data_buffer)
ax.set_ylim(0, 4095)  # ESP32 ADC is 12-bit (0–4095)
ax.set_title("Real-time Audio Waveform ")
ax.set_xlabel("Samples")
ax.set_ylabel("ADC Value")

try:
    while True:
        if ser.in_waiting > 0:
            try:
                value = int(ser.readline().decode().strip())
                data_buffer.append(value)
                line.set_ydata(data_buffer)
                ax.relim()
                ax.autoscale_view(True, True, False)
                plt.draw()
                plt.pause(0.01)
            except ValueError:
                pass  # Skip invalid data
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    ser.close()
    plt.ioff()
    plt.show()
