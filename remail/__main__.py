import remail.mail_utils as mail_utils
import remail.cli as cli
from decouple import config


def get_mail() -> mail_utils.Mail:
    content = cli.get_content()
    return mail_utils.Mail(*content.values())


def main() -> None:
    mail = get_mail()
    addresses = cli.get_addresses().values()
    password = config("PASSWORD", default=cli.get_password())
    mail_utils.send(mail, *addresses, password)


if __name__ == "__main__":
    main()
