

class firstClass:

    def fun(self):
        print("This is the class for the public")

    def __fun(self):
        print("This is private")

    def helpMe(self):
        self.fun()
        self.__fun()

obj = firstClass()
obj.helpMe()


class Scores:
    def __init__(self):
        self._studentScore =0

obj = Scores()
obj._studentScore = 78
print(obj._studentScore)

class medicalHistory:

    def __init__(self):
        self.__tstresults = 'Yes'

    def getResults(self):
        print(self.__tstresults)

    def setPrivate(self, private):
        self.__tstresults = private

obj = medicalHistory()
obj.getResults()
obj.setPrivate('no')
obj.getResults()
