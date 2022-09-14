from pprint import pprint
from vk import VK
from ya import YandexDisk
        
if __name__ == "__main__":
    access_token_vk = 'vk1.a.UScRFnHAxclJoyyt0inuNJd1rDGyQb6ZRX3V37WvoX5sYUMSMFfSse8dVNltUfSKysiJ7-T3e_opBDoSLIlpc8BN7-i2rU1RF-fUG8ZRFMiGffX7ViAmBJVKZNQJwmQWllBmr7-rPwzQZtV-69SKrx3FL19I1d-nx6jL7LVonCRZHdCUmdhA2WQI0sPZu2FR'
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
