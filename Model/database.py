from Model.hobby import Hobby
from Model.proton import Proton


class Database:
    def __init__(self):
        # Note that this is a list of Protons objects,
        # not protons names
        self.protons = []
        # Note that this is a list of Hobbies objects,
        # not hobbies titles
        self.hobbies = []

    def addHobby(self, hobby: Hobby):
        pass

    def registerProton(self, name, age, track: Proton):
        createdproton = name, age, track
        self.protons.append(createdproton)

    def findHobby(self, hobbyTitle: str):
        # TODO
        pass

    def findProton(self, protonName: str):
        # TODO
        pass

    def deleteProton(self, protonName: str):
        # TODO
        pass

    def deleteHobby(self, hobbyName: str):
        # TODO
        pass
