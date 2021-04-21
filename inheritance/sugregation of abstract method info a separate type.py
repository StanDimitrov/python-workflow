from abc import ABC, abstractmethod
class Bird:
    def __init__(self,name):
        self.name = name

class Flyable(ABC):
    @abstractmethod
    def start_flight(self):
        pass
    @abstractmethod
    def stop_flight(self):
        pass

class Eagle(Bird,Flyable):
    def __init__(self, name, master_name):
        super().__init__(name)
        self.master_name = master_name

    def start_flight(self):
        print('Eagle: ', self.name, 'started his own flight')

    def stop_flight(self):
        print('Eagle: ', self.name, 'stopped his onw flight')

class Own(Bird,Flyable):
    def __init__(self, name,night_vision_power):
        super().__init__(name)
        self.night_vision_power = night_vision_power

    def start_flight(self):
        print('Own: ', self.name, 'started its own flight')

    def stop_flight(self):
        print('Own: ', self.name, 'stopped its onw flight')

class Kiwi(Bird):
    def __init__(self,name, power):
        super().__init__(name)
        self.power = power

class Airplane(Flyable):
    def __init__(self,make, fuel_capacite):
        self.make = make
        self.fuel_capacite = fuel_capacite

    def start_flight(self):
        print('Ariplane: ', self.make, 'started flight')

    def stop_flight(self):
        print('Airplane: ', self.make, 'stopped flight')

class Game:
    def __init__(self):
        self.game_objects = [Kiwi('Sweety',10),Eagle('Roky','Balboa'),Own('Rouge eye',90),Airplane('Boeing',1000)]

    def start_game(self):
        for b in self.game_objects:
            if isinstance(b,Flyable):
                b.start_flight()

    def stop_game(self):
        for b in self.game_objects:
            if isinstance(b,Flyable):
                b.stop_flight()

g = Game()
g.start_game()
g.stop_game()