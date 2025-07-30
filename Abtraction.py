from abc import ABC,abstractmethod
class bike(ABC):
    @abstractmethod
    def add(self):
        pass
class price(bike):
    def __init__ (self,name,pluspoint):
        self.name=name
        self.pluspoint=pluspoint
    def add(self):
        return self.name + self.pluspoint
c=bike("inter","stellar")
print("Adding",c.add())

        