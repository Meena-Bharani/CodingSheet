
class Microwave:
    def __init__(self):
        pass
    def heat_food(self):
        print('heated.....')

class Dishwasher:
    def __init__(self):
        pass
    def wash_dishes(self):
        print('washed.....')


class Kitchen:
    def __init__(self):
        self.microwave = Microwave()
        self.dishwasher = Dishwasher()

        self.microwave_methods = [f for f in dir(Microwave) if not f.startswith('_')]
        self.dishwasher_methods = [f for f in dir(Dishwasher) if not f.startswith('_')]
    
    # def heat_food(self):
    #     self.microwave.heat_food()
    
    # def wash_dishes(self):
    #     self.dishwasher.wash_dishes()
    
    def __getattr__(self,func):
        def method(*args):
            if func in self.microwave_methods:
                return getattr(self.microwave,func)(*args)
            elif func in self.dishwasher_methods:
                return getattr(self.dishwasher,func)(*args)
            else:
                raise AttributeError
        return method

if __name__=='__main__':
    kitchen=Kitchen()
    kitchen.heat_food()
    kitchen.wash_dishes()

    # dw = Dishwasher()
    # print(dir(dw))

