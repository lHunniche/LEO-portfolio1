cd /home/pi/scripts/
echo "Starting server"
python3 blink_server.py &
echo "Starting network listener"
socat tcp-listen:8080,reuseaddr,fork exec:"python3 swap_state.py" &
echo "Starting button listener"
python3 button_swap.py &
