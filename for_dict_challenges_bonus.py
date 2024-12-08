"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# Задание 1. Вывести айди пользователя, который написал больше всех сообщений.
def most_messages_user(messages):
    message_count = {}
    for item in messages:
        user_id = item['sent_by']
        if user_id not in message_count:
            message_count[user_id] = 0
        else:
            message_count[user_id] += 1

    max_user = None
    max_count = 0
    for user_id in message_count:
        count = message_count[user_id]
        if count > max_count:
            max_user = user_id
            max_count = count

    return f"Пользователь {max_user}: написал {max_count} сообщений. Больше всех!"

#Задание 2. Вывести айди пользователя, на сообщения которого больше всего отвечали (Переделать)

''''def most_reponded_user(messages):
    reply_count = {}
    for item in messages:
        the_most_popular_message_id = item['reply_for']
        user_id = the_most_popular_message_id['sent_by']

        #reply_count[the_most_popular_message_id] = reply_count.get(the_most_popular_message_id, 0)+1

        max_user = None
        max_answer_count = 0
        for the_most_popular_message_id in reply_count:
            count = reply_count[the_most_popular_message_id]
            if count > max_answer_count:
                max_user = user_id
                max_answer_count = count
    return f'Пользователь {max_user} на свои сообщения получил {max_answer_count} ответов. Больше всех!'  '''''




if __name__ == "__main__":

    messages = generate_chat_history()
    print(messages)

    print(most_messages_user(messages))
    print()









