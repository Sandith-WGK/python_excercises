import requests
import time
import passValueThread
from queue import Queue

def get_image_urls(count):
    # Early return if invalid count provided
    if count <= 0:
        return
    
    # Generate URLs for images with sequential IDs
    for i in range(0, count):
        url = f'https://picsum.photos/id/{i}/200/300'
        yield url

# Record start time in nanoseconds for precise timing
start = time.time_ns()

# Generate URLs for 1 image (modify this number to download more images)
urls = list(get_image_urls(100))

num_threads = 10
urls_list = []

for i in range(0,len(urls),num_threads):
    l = urls[i:i+num_threads]
    urls_list.append(l)

threads = []
results = Queue()

for i in range(0, num_threads):
    thread = passValueThread.ImageDownloader(i, f"Thread-{i}", urls_list[i],results)
    thread. start()
    threads.append(thread)

for thread in threads:
    thread.join()

total = 0

while not results.empty():
    total += results.get()
# Calculate total execution time
diff = time.time_ns() - start

print(f"{total} images are successfully downloaded.")
# Display execution time in milliseconds
print("Duration : ", diff/1000000)  