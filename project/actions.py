from project.Api.api_vk_method import VkApiMethods

from project.utils import date_to_unix
from project.Api.access_data import AccessData
from project.pic.path_to_pic import PATH_TO_PIC
from project.Api.api_vk_data import ApiData

TEXT = 'this is test message'
OWNER_ID = AccessData.OWNER_ID
DATE = '2023-06-11 12:47:00'
PUB_DATE = date_to_unix(DATE)


def add_post_with_pic():
    # получаем url загрузки, создавая при этом экземпляр VkApiMethods
    upload_url = VkApiMethods(api_url=ApiData.API_URL,
                              token=AccessData.TOKEN,
                              api_version=ApiData.API_VERSION).get_upload_url()

    # без создания экземпляра класса?
    photo, server, photo_hash = VkApiMethods(api_url=ApiData.API_URL,
                                             token=AccessData.TOKEN,
                                             api_version=ApiData.API_VERSION).send_pic_to_url(
        upload_url=upload_url, image_path=PATH_TO_PIC)

    user_id, photo_id, url = VkApiMethods(api_url=ApiData.API_URL,
                                          token=AccessData.TOKEN,
                                          api_version=ApiData.API_VERSION).save_photo_before_post(photo=photo,
                                                                                                  server=server,
                                                                                                  photo_hash=photo_hash)
    post_id = VkApiMethods(api_url=ApiData.API_URL,
                           token=AccessData.TOKEN,
                           api_version=ApiData.API_VERSION
                           ).post_on_wall(
                           text=TEXT, owner_id=OWNER_ID, user_id=user_id, publish_date=PUB_DATE, pic_id=photo_id)

    return post_id
