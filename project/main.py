from actions import add_post_with_pic
from project.Api.access_data import AccessData
import vk_api

#TODO проверить как от имени группы постить
#TODO написать сообщения как посылать пользователям сообщения
#TODO зайти в репозиторий чип трип дпта, проверить бранч сэйн
#TODO Связаться с Димой, подготовить функцию, которая будет принимать данные для бота

# 2 разных варианта, по разному обращаться к ним
session = vk_api.VkApi(token=AccessData.TOKEN)
vk = session.get_api()
attachment = 'photo5958128_457239818'


# TODO почитать про random id
def send_massage(user_id, message=None, attachment=None):
    vk.messages.send(user_id=user_id, random_id=0, message=message, attachment=attachment)


# send_massage(user_id=53024259, message='MASSAGE', attachment=attachment)
add_post_with_pic()