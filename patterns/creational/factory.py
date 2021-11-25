from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Car(Transport):
    def deliver(self):
        print("Car...")


class Boat(Transport):
    def deliver(self):
        print("Boat...")


class LogisticBase(ABC):
    @abstractmethod
    def create_transport(self, type_):
        pass


class Logistic(LogisticBase):
    def create_transport(self, type_):
        if type_ == "car":
            return Car()
        elif type_ == "boat":
            return Boat()


if __name__ == '__main__':
    logist = Logistic()

    logist.create_transport("car").deliver()
    logist.create_transport("boat").deliver()
