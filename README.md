Example1 and Example2 are two simple examples of how to use the Artemis smartwatch board.

Example1:
<video src="https://github.com/user-attachments/assets/e6fb9160-971b-4a9b-a4c5-5cf510c29ed5" width="300" />


The Artemis and CircuitOS libraries are included in this repository ONLY for reference, to better understand the code, as no official documentation exists. By looking at this source code, you can pull out these functions and use them in your own projects. I've consolidated a list here, but feel free to take a look yourself, and make a pr if you find anything missing or incorrect.

Here is the official codebase I got the answers from: https://github.com/CircuitMess/micropython

Feel free to follow this medium article to get set up: https://medium.com/@nplaneta03/i-got-to-host-a-workshop-on-programming-a-smartwatch-1a0f1c5778d0

Or follow the general micropython setup guide: https://github.com/CircuitMess/micropython

|Command                                                       |Description                                                                                     |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|begin()                                                       |Hardware Initializes the Artemis hardware. Must be called first in every script after importing.|
|backlight.on() //or off                                       |Turns the backlight on or off.                                                                  |
|display.fill(color)                                           |Display Fills the entire screen. display.fill(0) clears the screen to black.                    |
|display.rect(x, y, width, height, color, filled)              |Display Draws a rectangle. filled is a True/False boolean.                                      |
|display.ellipse(x, y, rx, ry, color, filled)                  |Display Draws an oval/circle. rx and ry are horizontal/vertical radii.                          |
|display.text('string', x, y, color)                           |Display Prints text to the screen at the given coordinates.                                     |
|display.blit(buffer, x, y, transparent_color)                 |Display Draws a complex graphic (like a sprite) using a FrameBuffer.                            |
|display.commit()                                              |Display Crucial: Pushes drawings to the actual screen. Required to update the display.          |
|Display.Color.[Color]                                         |Display Built-in colors: Red, Green, Blue, Yellow, Magenta, Cyan, White.                        |
|buttons.scan()                                                |Input Crucial: Reads physical buttons. Must be inside the while True loop.                      |
|buttons.on_press(button, function)                            |Input Links a button press to a function (callback).                                            |
|Buttons.[Name]                                                |Input Physical buttons: Buttons.Up, Buttons.Down, Buttons.Select, Buttons.Back.                 |
|imu.get_accel_x()                                             |Sensors Returns acceleration in the x direction.                                                |
|imu.get_accel_y()                                             |Sensors Returns acceleration in the y direction.                                                |
|imu.get_accel_z()                                             |Sensors Returns acceleration in the z direction.                                                |
|imu.get_gyro_x()                                              |Sensors Returns tilt in x direction (Pitch: tilting wrist up/down).                             |
|imu.get_gyro_y()                                              |Sensors Returns tilt in y direction (Roll: twisting forearm).                                   |
|imu.get_gyro_z()                                              |Sensors Returns tilt in z direction (Yaw: sweeping arm left/right).                             |
|piezo.tone(frequency, duration)                               |Audio Plays a note. Frequency in Hertz, duration in milliseconds.                               |
|for i in range(6):  leds[i].on() // or off                    |LEDs Turns specific LEDs (0-5) on or off.                                                       |
|rgb.set(r, g, b)                                              |LEDs Sets the secret LED at the front (values 0 or 100).                                        |
|time.sleep(seconds)                                           |Utilities Pauses execution for a specified number of seconds.                                   |
|rtc.set_time(Time())                                          |Time Sets the time on the watch.                                                                |
|rtc.get_time()                                                |Time Gets the current time from the watch.                                                      |
|rtc.get_time().{property}                                     |Time Access time properties: hours, minutes, seconds, month, day, year.                         |
