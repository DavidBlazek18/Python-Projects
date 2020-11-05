

class Person:
        def __init__(self):
                self._phoneNumber = "111-111-1111"
                self.__birthDate = "9/9/2020"
               
                               
        def getbirthDate(self):
                print(self.__birthDate)

        def setbirthDate(self, private):
                self.__birthDate = private

obj = Person()
obj._phoneNumber = "222-222-2222"
print(obj._phoneNumber)         # Can change a Protected variable outside of the class.
obj.getbirthDate()
obj.setbirthDate("10/10/2020")  # Have to SET the method then GET the method to change Private variable ouside of class.
obj.getbirthDate()              # Private date gets changed to 10/10/2020.
obj.__birthDate = "123"         # Note: If try to change date outside of class it won't work.
obj.getbirthDate()              # Still 10/10/2020.




    
 
