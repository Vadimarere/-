import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "a4265e9378b3ecd8ae86217cae09e1b62bb46d54cef60f782bdef19d5edb1dfd85ddc94d91410113adab7"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            
            if text == "начать":
                send_message(user_id,"не буду начинать,хахахахах ладно я пошутил)")
            
