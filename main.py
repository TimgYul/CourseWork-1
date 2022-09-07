import requests
from pprint import pprint
import json
import os
import progressbar as pb
import urllib.request

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


class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id 
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    def download_from_vk(self,folder, ya):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'extended': 1, 'count': 1000}
        response = requests.get(url, params={**self.params, **params})
        bar = pb.ProgressBar(max_value = response.json()['response']['count'])
        list = []
        num = 0
        
        for rep in response.json()['response']['items']:            
            result = {}
            result['file_name'] = f'{rep["likes"]["count"]}-{rep["date"]}.jpg'
            result['size'] = 'z'
            list.append(result)
            num += 1
            urllib.request.urlretrieve(rep["sizes"][-1]["url"],result['file_name'])
            ya.upload_file_to_disk(result['file_name'])
            os.remove(result['file_name'])
            bar.update(num)
            
        json_data = json.dumps(list)

        return 'Done'#json_data 
        

access_token_vk = ''
user_id = input('Введите ID пользователя VK: ')
access_token_ya = input('Введите токен с Полигона Яндекс.Диска:')

ya = YandexDisk(token=access_token_ya)
vk = VK(access_token_vk, user_id)

print(vk.users_info())
name = 'photos_vk'
if (os.path.exists(name)):
    os.chdir(name)
    #print(f'Создана папка {name}!')
else:
    try:
        os.mkdir(name)
        #print(f'Создана папка {name}!')
        os.chdir(name)
    except OSError:
        #print(f'Проблема с созданием папки {name}!')
        exit()
print('Загрузка началась!')
vk.download_from_vk(name, ya)
print(' Все прошло успешно!')
