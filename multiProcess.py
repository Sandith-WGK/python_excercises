#from threading import Thread
from multiprocessing import Process
import requests

class ImageDownloader(Process): # Inherits from Process, not Thread
    def __init__(self,name,threadId,urls,results):
        super(ImageDownloader,self).__init__()

        self.id = threadId
        self.name = name
        self.urls = urls
        self.sucusess_count = 0
        self.results = results

    def run(self):
        for i,url in enumerate(self.urls):
            if self.download_img(url,f'{self.id}-{i}'):
                self.sucusess_count += 1

        self.results.put(self.sucusess_count)   

    def download_img(self,url,i):
    
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
            return True
        else:
            # Log failure if HTTP request unsuccessful
            print('Image Couldn\'t be retrieved')
            return False    