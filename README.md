# CV_tools_for_event-based_camera
Some tools-code in my project
## Notice
1. These 4 programs are used in my project as some tools so I push them here in order to avoid rewriting them again.</br></br>
2. The file "change_speed" is a program to change the play speed for videos.</br></br>
3. The "video_capture" is a program to capture the frames in the video.</br></br>
4. In an event camera, each event e is represented as a tuple (u, v, t, p), where u and v are the pixel coordinates and t is
the timestamp of the event, and p = ±1 is the polarity of the event, which is the sign of the brightness change (p = 0 for no event). There are 2 simple ways to observe the stream of events: The first way is stacking Based on Time (SBT). So the "insert_num.py" stacks the events based on a fixed time interval with the different colors corresponding to the types of "p". "insertnum_only_1_color.py" do the same thing but use the same color no matter the "p" is "+1" or "-1". And the ohter way is Stacking Based on the number of Events (SBE). I don't push the program here but you can change the insert_num.py.</br></br>
5. I think SBE-way is more easy to observe than SBT. In addition, for science research, the "Overlapping Spatio-temporal Window" way is better than SBE or SBT which stacks events based on the number of events but has some overlap for example the same N events are used in two adjacent frames (N can set by user). I will upload the code of this way next time beacuse it's in another computer.</br></br>
6. Welcome to contact me for more academic communications.
