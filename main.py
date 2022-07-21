from bot import wish_user,speak,takeCommand,BOT_NAME,USER_NAME
from functions import online_ops,os_ops,offline_ops
if __name__ == '__main__':
    wish_user()
    while True:
        query = takeCommand().lower()

        if f"{BOT_NAME}" in query:
            query = query.replace(f"{BOT_NAME}", "")

        if "great me" in query or "wish me" in query:
            wish_user()
