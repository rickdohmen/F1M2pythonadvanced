

class mijnclass:

    varopenbaar = "dit is openbaar toegankelijk"
    __varprive = "deze is prive"

    def voorbeeld (self):
        print(self.__varprive)

        waardeA = "tijdelijk"

        print("waardeA is:", waardeA)
        #vanaf dit punt stopt de functie en bwstaat waardeA niet meer

    def anderefunctie(self):
        #waardeA bestaat aleen in functie "voorbeeld"
        #print(waardeA)

        #vanaf dit punt voeg ik een nieuwe variabele toe aan de instancie van deze class
        self.nieuwevariabele = "dit is een nieuwe variabele"

instClass = mijnclass()
print(instClass.varopenbaar)

instClass.voorbeeld()
instClass.anderefunctie()