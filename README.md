# LEO-portfolio1

The traffic light logic is contained in "traffic_light.py", where it continously reads the state of "state.txt".  
When "state.txt" contains "0", the traffic light shows red. When it contains "1", it shows green.  
Swapping the value from 0 to 1, or vice versa, triggers a transition from green to red, or red to green.  

A socat tcp server listens on port 8080 for requests. When it receives traffic, it runs the "swap_state.py" python script.  
This scripts does as it says on the tin - if the current state is 0 it becomes 1, and if it is 1 it becomes 0.  

The "swap_state.py" script is also the script that is called, when the button is pressed. The button logic is contained in "button_swap.py".  
Only thing it does is wait for a button press. Following a button press it runs the "swap_state.py" script, and then waits for another press.  

Everything is started with the "start_whole_thing.sh" script. 

WARNING: Assignment asks that the Green LED is on from the start. This solution, however, starts with the Red light turned on.