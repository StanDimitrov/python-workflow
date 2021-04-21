from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def flight(self):
        pass

    @abstractmethod
    def stop_flight(self):
        pass

class Eagle(Bird):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def flight(self, start_flying_power):
        self.start_flying_power = start_flying_power
        print('Eagle: ', self.name,'Started flying ', 'with: ', start_flying_power)

    def stop_flight(self,power_view):
        self.power_view = power_view
        print('Eagle:',self.name, 'stopped hie flight', 'the ELG001 have', self.power_view, 'power_view', 'and',self.power,'power')

class Game:
    def __init__(self):
        self.bird_objects = [Eagle('E001',99)]

    def start_game(self):
        for b in self.bird_objects:
            b.flight(9)

    def stop_game(self):
        for b in self.bird_objects:
            b.stop_flight(88)

# e = Eagle('EGL001',98)
# e.flight(20)
# e.stop_flight('excellent')

g = Game()
g.start_game()
g.stop_game()