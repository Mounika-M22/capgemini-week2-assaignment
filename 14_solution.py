# Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        return f'notification sent'
class Emailnotification(Notification):
    def send(self):
        print(super().send()+ " " + "through email")
class Smsnotification(Notification):
    def send(self):
        print(super().send()+ " " + "through sms")
obj1=Smsnotification()
obj1.send()

obj2=Smsnotification()
obj2.send()
