from project.Api.access_data import AccessData
from project.pic.path_to_pic import PATH_TO_PIC
import datetime as DT
import requests
import os


TEXT = 'this is test message'
OWNER_ID = AccessData.OWNER_ID
DATE = '2023-06-05 22:43:00'
PIC_PATH = '/cat.jpg'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PATH_TO_PIC = os.path.join(DIR_PATH + PIC_PATH)

class ApiData:
    API_URL = 'https://api.vk.com/method/'
    PIC_UPLOAD_ON_SERVER = 'photos.getWallUploadServer'
    PIC_SAVE_BEFORE_POST = 'photos.saveWallPhoto'
    # EDIT_WALL_POST = 'wall.edit'
    POST_ON_WALL = 'wall.post'
    # CREAT_COMMENT = 'wall.createComment'
    # GET_POST_LIKES = 'wall.getLikes'
    # DELETE_POST = 'wall.delete'
    API_VERSION = 5.131


class VkApiMethods:

    def __init__(self, api_url, token,
                 api_version, user_id=None, domain=None):
        self.api_url = api_url
        self.token = token
        self.api_version = api_version
        self.user_id = user_id
        self.domain = domain

    # здесь и нужен домен, смысл не понятен
    def post_on_own_wall(self, text, owner_id=None, pic_id=None):
        resp_post = requests.post(self.api_url + ApiData.POST_ON_WALL,
                                  params={
                                      "access_token": self.token,
                                      "v": self.api_version,
                                      "domain": self.domain,
                                      "message": text,
                                      "attachments": f'photo{owner_id}_{pic_id}'
                                     }
                                  ).json()
        return resp_post["response"]["post_id"]

    # тоже постит на своей странице
    def post_on_wall(self, text, owner_id, user_id, publish_date=None, pic_id=None):
        if publish_date is not None:
            publish_date = date_to_unix(publish_date)
        resp_post = requests.post(self.api_url + ApiData.POST_ON_WALL,
                                  params={
                                      "access_token": self.token,
                                      "owner_id": owner_id,
                                      "message": text,
                                      "publish_date": publish_date,
                                      "attachments": f'photo{user_id}_{pic_id}',
                                      "v": self.api_version,
                                     }
                                  ).json()

        return resp_post["response"]["post_id"]

    def get_upload_url(self):
        resp_url = requests.post(self.api_url + ApiData.PIC_UPLOAD_ON_SERVER,
                                 params={
                                     "access_token": self.token,
                                     "v": self.api_version,
                                 }
                                 ).json()
        print(resp_url)
        return resp_url["response"]["upload_url"]


    @staticmethod
    def send_pic_to_url(upload_url, image_path):
        file = {"file1": open(f"{image_path}", "rb")}
        response_photo = requests.post(upload_url, files=file).json()
        return (response_photo["photo"],
                response_photo["server"],
                response_photo["hash"])

    def save_photo_before_post(self, photo, server, photo_hash):
        save_photo = requests.post(self.api_url + ApiData.PIC_SAVE_BEFORE_POST,
                                   params={
                                       "access_token": self.token,
                                       "v": self.api_version,
                                       "user_id": self.user_id,
                                       "photo": photo,
                                       "server": server,
                                       "hash": photo_hash
                                     }
                                   ).json()
        return (save_photo["response"][0]["owner_id"],
                save_photo["response"][0]["id"],
                save_photo["response"][0]["sizes"][5]["url"])


def date_to_unix(date: str):
    dt = DT.datetime.fromisoformat(date)
    return dt.timestamp()


def add_post_with_pic(pub_date=None):
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
                           text=TEXT, owner_id=OWNER_ID, user_id=user_id, publish_date=pub_date, pic_id=photo_id)

    return post_id