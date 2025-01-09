### Signal Conversions

After parsing the hand movements the raspberry pi needs to send them to the arduino before it can be sent to the computer. In doing this, the pi will send numbers associated with various keys and mouse commands that will be parsed/interpreted by the arduino then executed on your machine. Here are the key codes.


| Value (String)                        | Command                                                |
|---------------------------------------|--------------------------------------------------------|
| 10                                    | middleMouseDown                                        |
| 11                                    | middleMouseUp                                          |
| 20                                    | leftMouseDown                                          |
| 21                                    | leftMouseUp                                            |
| 30                                    | rightMouseDown                                         |
| 31                                    | rightMouseUp                                           |
| 123456788                             | move_start                                             |
| Numbers sent while movement is active | move(x,y) ; They are received as alternating x-y pairs |
| 123456789                             | move_end                                               |
| 404                                   | stop mouse control                                     |

 
I should probably use a regex to read x/y coords, but I don't have too much time to implement it. I will probably come back and optimize this later. 