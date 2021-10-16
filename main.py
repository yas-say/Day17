class Student:
    def __init__(self, userid, username):
        print("User being created")
        self.userid = userid
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


student1 = Student(1, "Yas1")
print(str(student1.userid) + " " + student1.username)

student2 = Student(2, "Moh")
print(str(student2.userid) + " " + student2.username)

student1.follow(student2)

print(student1.follower)
print(student1.following)
print(student2.follower)
print(student2.following)
