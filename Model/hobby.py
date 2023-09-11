from Model.proton import Proton

class Hobby:
    def __init__(self,title: str,imagePath: str):
        self.title = title
        self.imagePath = imagePath
        #Note that this is a list of Protons objects, 
        #not protons names
        self.hobbyProtons = []

    def addProton(self,proton: Proton):
        #TODO
        pass

    def removeProton(self,protonName : str):
        #TODO
        pass


