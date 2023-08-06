import os
import pickle
from search_users_test import save_index
import logging
import vk_api

logging.basicConfig(filename='exceptions.log', level=logging.ERROR)

token = 'vk1.a.GejAv1tQrm4gotI8uRxENm13sEobFKmXHrelkefVpEr-31wzVVqv5bI80I5quXwOFPZLpo2EqMPyviFI4Es4W8hcRzOmLHBwbvdBXLrxOMw7ji36KtNNAzfAb4Catq3EXaxjqNcXmJGIyIV_rBUeCNt15_jcSvaY0F2uADg76sJvOd7y9K_ka_HEAtLmkf4yGrgpYbWmE3anU3xt6gZ1Mg'
b_t_f_token = 'vk1.a.jV5hHc9PQokcaDv3bG403FHEfGQetbvZFEbnWH0FjRFGA9r6ywGfguVYfxdw55N157y7Tt1ekUF47gqKZ-9qcc4VN1gtn4yIE7MaDOXkDdrfL0Hohv22RdZpu2tcf85e_a4NWzsiSTwUmfXVDHuvv3tRgx5CNNGsOqv6ClOcv7--XJjXKVZYiI29h9qHfKjKJEK-_qCVHuPtx1l6OKRK7g'
message = '''
Привет, дорогие друзья! 🌍🚀 
 
У нас есть отличные новости для всех любителей путешествий! Мы хотим представить вам CheapTrip — вашего надежного помощника в путешествиях. 🌟 
 
Планируйте поездки даже без подключения к интернету!
https://bustrainflight.cheaptrip.guru
CheapTrip - это удивительное мобильное приложение, доступное для установки на Android. Теперь вы можете получить доступ к значительно большему количеству функциональности прямо на своем смартфоне! 📱🌐📝 
 
Что вы можете ожидать от CheapTrip? Это приложение поможет вам найти самые дешевые маршруты между городами, сочетая разные виды транспорта, хостели, отели и многое другое. Вы сможете легко и удобно планировать свои путешествия, сравнивать цены и получать эксклюзивные предложения. ✈️🏨🚗 
 
Однако это еще не все! Мы также предлагаем вам посетить наши страницы в соц сетях, где есть много информации об аттракциях для бюджетных путешественников:
https://www.facebook.com/cheaptripguru 
https://www.linkedin.com/company/cheaptrip 
https://instagram.com/cheaptrip.guru 
https://vk.com/cheaptripguru 
https://t.me/bustrainflightferry
 
Так что не упустите возможность использовать CheapTrip, чтобы сделать свои путешествия более доступными, увлекательными и удобными! Установите наше мобильное приложение bustrainflight.cheaptrip.guru прямо сейчас и посетите наш веб-сайт https://cheaptrip.guru, чтобы начать свое следующее незабываемое приключение. 🌍✈️ 
 
Спасибо, что выбрали CheapTrip! Мы с нетерпением ждем ваших отзывов и надеемся, что наше приложение и веб-сайт принесут вам удовольствие и помогут в каждом вашем путешествии. С наилучшими пожеланиями, команда CheapTrip. 🌟🎉'''


def upload_photo(att_path, photo, session):
    file_path = os.path.join(att_path + '/' + photo)
    upload = vk_api.VkUpload(session)
    photo = upload.photo_messages(file_path)
    photo_data = photo[0]
    owner_id = photo_data['owner_id']
    photo_id = photo_data['id']
    access_key = photo_data['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def send_massage(token, user_id, message=None, attachment=None, att_path=None):
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    if attachment is not None:
        attachment = upload_photo(att_path=att_path, photo=attachment, session=session)
    vk.messages.send(peer_id=user_id, random_id=0, message=message, attachment=attachment)


# чтение pkl файла
def read_pkl():
    with open('users.pkl', 'rb') as f:
        data = pickle.load(f)

    print(len(data[0]))
    print(data)


# загружает users из файла
def load_data():
    if os.path.exists('users.pkl'):
        with open('users.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return []


# загружает index из файла
def load_index():
    if os.path.exists('index.pkl'):
        with open('index.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return 0  # возвращаем 0, если файл с индексом не существует


def process_users(users, index):
    for i in range(index, min(index + 19, len(users))):
        user = users[i]
        try:
            send_massage(user_id=user['id'], message=message, token='vk1.a.IPGGZagk25fJoYDWwH9VGbN9FLeZjZEDcaH5OOrxLhvUpKFr85BfLMR62KFEmyr_oC29PoRzuOz-1tosp5ku6RHCHd3iEmsR08WNY6ug-BmcTaLaaS7FCoi3KAsAXuWz8jHH8dVpnVUBku0pHtup_jgVaWbib4k_L4gPP_Ps-3T3iHrTV16cJHutMMM56evX7d4sr6Gdbf8zu_fIQwkRdQ')
        except Exception as e:
            logging.error(f"ID - {user['id']}: {str(e)}")
            continue
    return i + 1  # новый индекс после обработки


users = load_data()

# for user in users:
#     print(user)


def send_19_users():
    users = load_data()
    index = load_index()
    new_index = process_users(users=users, index=index)
    save_index(new_index)


# save_index(46)
index = load_index()
print(index)

send_19_users()
print(index)

# dir_path = os.path.dirname(os.path.realpath(__file__))
# '''Отправляет от имени группы, если уже переписывался, по крайней мере мне'''
# send_massage(user_id=53024259, message='MASSAGE', attachment='cat.jpg', att_path=dir_path, token='vk1.a.GejAv1tQrm4gotI8uRxENm13sEobFKmXHrelkefVpEr-31wzVVqv5bI80I5quXwOFPZLpo2EqMPyviFI4Es4W8hcRzOmLHBwbvdBXLrxOMw7ji36KtNNAzfAb4Catq3EXaxjqNcXmJGIyIV_rBUeCNt15_jcSvaY0F2uADg76sJvOd7y9K_ka_HEAtLmkf4yGrgpYbWmE3anU3xt6gZ1Mg')
# send_massage(user_id=237417835, message=message, att_path=dir_path, token='vk1.a.IPGGZagk25fJoYDWwH9VGbN9FLeZjZEDcaH5OOrxLhvUpKFr85BfLMR62KFEmyr_oC29PoRzuOz-1tosp5ku6RHCHd3iEmsR08WNY6ug-BmcTaLaaS7FCoi3KAsAXuWz8jHH8dVpnVUBku0pHtup_jgVaWbib4k_L4gPP_Ps-3T3iHrTV16cJHutMMM56evX7d4sr6Gdbf8zu_fIQwkRdQ')
# users = search_all_users(token=token, city_name=295)
# for user in users:
#     id = user['id']
#     try:
#         send_massage(user_id=id, message=message, attachment='logo.jpg', att_path=dir_path, token=b_t_f_token)
#         print(id, '- done')
#     except Exception as exc:
#         with open('error_log.txt', 'a') as f:  # 'a' обозначает добавление в файл, а не его перезапись
#             f.write(str(id) + str(exc) + '\n')  # записываем информацию об исключении в файл

