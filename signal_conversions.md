### Signal Conversions

After parsing the hand movements the raspberry pi needs to send them to the arduino before it can be sent to the computer. In doing this, the pi will send numbers associated with various keys and mouse commands that will be parsed/interpreted by the arduino then executed on your machine. Here are the key codes.


| Value     | Command              |
|-----------|----------------------|
| 10        | middleMouseDown      |
| 11        | middleMouseUp        |
| 20        | leftMouseDown        |
| 21        | leftMouseUp          |
| 30        | rightMouseDown       |
| 31        | rightMouseUp         |
| move(x,y) | move(x_dist, y_dist) |
 
