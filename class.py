#Class for Students

class Students:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

#method
    def change_name(self,new_name):
        self.name = new_name

    def change_age(self,new_age):
        self.age = new_age

    def add_tracks(self,new_tracks):
        self.tracks = new_tracks

    def get_score(self):
        if isinstance(self.age,int):
            print(self.name,self.age,self.tracks,self.score)
        else:
            print('Age must be int. Try again!')

Oluwaseyi = Students(name="Oluwaseyi", age=23, tracks="full stack", score=50.75)
#expected methods
Oluwaseyi.change_name("Jane")
Oluwaseyi.change_age(45)
Oluwaseyi.add_tracks("backend")
Oluwaseyi.get_score()
