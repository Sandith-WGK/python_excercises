from threading import Thread
import requests

class ImageDownloader(Thread):
    def __init__(self,name,threadId,urls):
        super(ImageDownloader,self).__init__()

        self.id = threadId
        self.name = name
        self.urls = urls

    def run(self):
        for i,url in enumerate(self.urls):
            self.download_img(url,f'{self.id}-{i}')
           

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
        else:
            # Log failure if HTTP request unsuccessful
            print('Image Couldn\'t be retrieved')    