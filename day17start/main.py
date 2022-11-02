class User:

    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("yesha", "002")
user2 = User("guddu", "001")
user1.follow(user2)
user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.following)
print(user2.followers)
