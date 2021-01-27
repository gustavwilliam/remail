from PyInquirer import prompt

questions_addresses = [
    {
        "type": "list",
        "name": "sender_email",
        "message": "Select an email to send from",
        "choices": [
            "pyautoalerts@gmail.com",
        ],
    },
    {
        "type": "input",
        "name": "receiver_email",
        "message": "Receiver",
        "default": "0306guod@gapp.uddevalla.se",
    },
]

questions_content = [
    {
        "type": "input",
        "name": "subject",
        "message": "Subject line"
    },
    {
        "type": "editor",
        "name": "body",
        "message": "Write an email body",
        "eargs": {
            "editor": "vim",
            "ext": "txt",
        }
    },
]

questions_password = [
    {
        "type": "input",
        "name": "password",
        "message": "Password",
    }
]


def get_addresses() -> dict:
    addresses = prompt(questions_addresses)
    return addresses


def get_content() -> dict:
    content = prompt(questions_content)
    return content


def get_password() -> str:
    answer = prompt(questions_password)
    return answer["password"]
