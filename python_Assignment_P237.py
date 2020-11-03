
from abc import ABC, abstractmethod
class Vaccine(ABC):
        def batchSize(self, amount):
                print("Your order amount: ",amount)

        @abstractmethod                 # The function is telling us to pass in an argument, but doesn't say how or what kind of data it will be.
        def shipment(self, amount):     # This abstract class cannot be instantiated, and
                pass                    # requires a subclass(es) to provide implementations for the abstract methods.


                                                # This is a subclass that inherits the Vaccine class attributes. This subclass 
class WalgreensPharmacyShipment(Vaccine):       # uses the @abstractmethod and provides implementations for the abstract method.                
        def shipment(self, amount):                            
                print('Your order of {} doses has exceeded your allotted amount of 300 doses.'.format(amount))


obj = WalgreensPharmacyShipment()
obj.batchSize(800)
obj.shipment(800)
        






    
 
