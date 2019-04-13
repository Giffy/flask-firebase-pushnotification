import requests
from models import User
from sqlalchemy import create_engine, orm

fcm_url = "https://fcm.googleapis.com/fcm/send"
headers = {
    "Content-Type": "application/json",
    "Authorization": "key=AAAAH8XAtB8:APA91bF77aujd6-XWzfsdwrBR7aIwpla2QmU1MtirzBgLyUm_n7NHtL_wp5p3kPpxQe8ZCN8FsyPAdTCgSyR8KVW8yKZJJ65KhbzU3gFI5UjxIjpFMa74d_NTIfiG3FW8Mma0TrA5LIW"
}
data = {
    "notification": {
        "title": "Push notification test",
        "body": "Test from Python",
        "click_action": "http://localhost:5000/list",
        "icon": "https://www.python.org/static/favicon.ico"
    },
}




def notify_all():
    engine = create_engine('sqlite:///notifications.db')
    session = orm.sessionmaker(bind=engine)()

    for record in session.query(User).all():
        data["to"] = record.token

        req = requests.post(fcm_url, json=data, headers=headers)
        print(req.json())


if __name__ == "__main__":
    notify_all()
