import threading
import demo_thread

# Create a thread
thread = threading.Thread(target=demo_thread.read_serial)

# Start the thread
thread.start()
while True:
    print(demo_thread.data_queue.get())
