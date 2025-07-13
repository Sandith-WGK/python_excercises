import requests
import time
import multiProcess
#from queue import Queue # process-safe queue for    processes
from multiprocessing import Queue # Process-safe queue for processes

def get_image_urls(count):
    # Early return if invalid count provided
    if count <= 0:
        return
    
    # Generate URLs for images with sequential IDs
    for i in range(0, count):
        url = f'https://picsum.photos/id/{i}/200/300'
        yield url
if __name__ == '__main__':# ← Essential for multiprocessing on Windows
    # All multiprocessing code goes here

    # Record start time in nanoseconds for precise timing
    start = time.time_ns()

    # Generate URLs for 1 image (modify this number to download more images)
    urls = list(get_image_urls(100))

    num_processes = 10
    urls_list = []

    for i in range(0,len(urls),num_processes):
        l = urls[i:i+num_processes]
        urls_list.append(l)

    processes = []
    results = Queue()

    for i in range(0, num_processes):
        process = multiProcess.ImageDownloader( f"process-{i}",i, urls_list[i],results)
        process.start()
        processes.append(process)

    for process in   processes:
        process.join()

    total = 0

    while not results.empty():
        total += results.get()
    # Calculate total execution time
    diff = time.time_ns() - start

    print(f"{total} images are successfully downloaded.")
    # Display execution time in milliseconds
    print("Duration : ", diff/1000000)  