from domains.attribute import att

class course(att):
    def __init__(self, id, name, mark):       
        super().__init__(id, name)
        self.__mark = mark
    def set_mark(self, mark):
        self.__mark = mark
    def get_mark(self):
        return self.__mark