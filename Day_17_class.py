class Car:
    def __init__(self, seats, doors):
        print("inside")
        self.seats = seats
        self.doors = doors


benz = Car(5, 6)
#benz.seats = 7
#benz.doors = 5
print(benz.seats, benz.doors)


class Insta:
    def __init__(self, id, username):
        self.user_id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = Insta(112,"Srikanth")
user_2 = Insta(132, "Harsha")
user_2.follow(user_1)

print("User 1: ", user_1.followers, user_1.following)
print("User 2: ", user_2.followers, user_2.following)
