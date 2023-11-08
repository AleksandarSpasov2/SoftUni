class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_self = False

    def send(self):
        self.is_self = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_self}"


final_emails = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    email_info = Email(sender, receiver, content)
    final_emails.append(email_info)
    command = input()

indexes = [int(s) for s in input().split(", ")]
for index in indexes:
    final_emails[index].send()

for current_email in final_emails:
    print(current_email.get_info())





