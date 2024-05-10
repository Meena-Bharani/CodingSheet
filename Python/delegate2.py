class Animal:
    def __init__(self,name,no_of_legs,sound):
        self.name = name
        self.no_of_legs = no_of_legs
        self.sound = sound
    
    def get_no_of_legs(self):
        print(f'I have {self.no_of_legs} legs')
    
    def get_sound(self):
        print(f'I sound {self.sound}')

class Dog(Animal):
    def __init__(self,name,no_of_legs,sound):
        super().__init__(name,no_of_legs,sound)
    
    def __getattr__(self,func):
        pass

if __name__=='__main__':
    dog = Dog('Fido',4,'bow bow')
    dog.get_no_of_legs()

    print(getattr(dog,'name'))
