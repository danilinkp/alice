from requests import post

raw = {
    "response": {
        "text": "Здравствуйте! Это мы, хороводоведы.",
        "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
        "card": {
            "type": "BigImage",
            "image_id": "1027858/46r960da47f60207e924",
            "title": "Заголовок для изображения",
            "description": "Описание изображения.",
            "button": {
                "text": "Надпись на кнопке",
                "url": "http://example.com/",
                "payload": {}
            }
        },
        "buttons": [
            {
                "title": "Надпись на кнопке",
                "payload": {},
                "url": "https://example.com/",
                "hide": True
            }
        ],
        "end_session": False
    },
    "session": {
        "session_id": "2eac4854-fce721f3-b845abba-20d60",
        "message_id": 4,
        "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
    "version": "1.0"
}

url = 'https://danilinck.herokuapp.com/post'
print(post(url, json=raw).json())
