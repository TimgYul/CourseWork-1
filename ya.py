import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        } 
    
    def create_folder(self):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': f'photos_vk', 'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        

    def upload_file_to_disk(self, filename):
        self.create_folder()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'photos_vk/{filename}', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href')

        response = requests.put(href, data=open(filename, 'rb'))


 