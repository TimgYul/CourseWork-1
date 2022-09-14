from pprint import pprint
from vk import VK
from ya import YandexDisk
import configparser  # импортируем библиотеку


if __name__ == "__main__":
    config = configparser.ConfigParser()  
    config.read("config.ini")
    access_token_vk =config["vk"]["token"]
    
    user_id = input('Введите ID пользователя VK: ')
    screen_name = input('Введите короткое имя пользователя VK: ')
    access_token_ya = input('Введите токен с Полигона Яндекс.Диска:')
    photo_count = int(input('Введите количество фото для загрузки:'))

    ya = YandexDisk(token=access_token_ya)
    vk = VK(access_token_vk, user_id,screen_name)

    print(vk.users_info())
    print('Загрузка началась!')
    vk.download_from_vk( ya, photo_count)    
    print(' Все прошло успешно!')
