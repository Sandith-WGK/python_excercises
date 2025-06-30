"""
Image Downloader Script

This script downloads random images from the Picsum Lorem Picsum service.
It fetches images by ID and saves them locally with timing information.

Dependencies:
    - requests: For HTTP requests
    - time: For performance timing
    - os: Implicitly used for file operations

Usage:
    Run the script to download images. Modify the count parameter in 
    get_image_urls() call to change the number of images downloaded.

Example:
    python image_downloader.py
"""

import requests
import time

# Base URL for Picsum Lorem Picsum service
# Format: https://picsum.photos/id/{image_id}/{width}/{height}
# Example: https://picsum.photos/id/237/200/300

def get_image_urls(count):
    """
    Generate image URLs from Picsum Lorem Picsum service.
    
    This function creates a generator that yields URLs for random images
    from the Picsum service. Each URL points to a 200x300 pixel image.
    
    Args:
        count (int): Number of image URLs to generate
        
    Yields:
        str: Complete URL for downloading an image
        
    Returns:
        None: If count is 0 or negative
        
    Note:
        Uses sequential IDs starting from 0. Some IDs may not exist
        on the Picsum service, which could result in download failures.
    """
    # Early return if invalid count provided
    if count <= 0:
        return
    
    # Generate URLs for images with sequential IDs
    for i in range(0, count):
        url = f'https://picsum.photos/id/{i}/200/300'
        yield url

def download_img(url, i):
    """
    Download an image from the given URL and save it locally.
    
    Downloads an image using HTTP GET request with streaming enabled
    to handle large files efficiently. Saves the image in the 'images' 
    directory with a numbered filename.
    
    Args:
        url (str): Complete URL of the image to download
        i (int): Index number used for filename generation
        
    Returns:
        None
        
    Side Effects:
        - Creates a file in the 'images' directory
        - Prints success or failure message to console
        
    Note:
        Assumes 'images' directory exists. Will raise exception if 
        directory doesn't exist.
    """
    # Make HTTP GET request with streaming enabled for memory efficiency
    res = requests.get(url, stream=True)

    # Generate filename using index parameter
    file_name = f'images/img{i}.jpg'

    # Check if request was successful (HTTP 200 OK)
    if res.status_code == 200:
        # Write image content to file in binary mode
        with open(file_name, 'wb') as f:
            f.write(res.content)
        print('Image sucessfully Downloaded: ', file_name)
    else:
        # Log failure if HTTP request unsuccessful
        print('Image Couldn\'t be retrieved')

# Record start time in nanoseconds for precise timing
start = time.time_ns()

# Generate URLs for 1 image (modify this number to download more images)
urls = get_image_urls(1)

# Download each image using the generated URLs
for i, url in enumerate(urls):
    download_img(url, i)

# Calculate total execution time
diff = time.time_ns() - start

# Display execution time in milliseconds
print("Duration : ", diff/1000000)