cd /home/pi/scripts/
echo "Starting traffic light"
python3 traffic_light.py &
echo "Starting network listener"
socat tcp-listen:8080,reuseaddr,fork exec:"python3 swap_state.py" &
echo "Starting button listener"
python3 button_swap.py &
