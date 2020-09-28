
#Parent class
class Airline_Passenger:
    name = "Chuck Yeager"
    email = "Yeager@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if entry_email == self.email and entry_password == self.password:
            print("Welcome to SpaceForce Airlines, {}".format(entry_name))   
        else:
            print("Please enter the correct email or password.")

#Child class Frequent Flyer
#This gives a 20% discount and asks for an additional code so the
#passenger can identify as a frequent flyer
class Frequent_Flyer(Airline_Passenger):
    miles_flown = 50000
    frequent_flyer_discount = 0.2
    frequent_flyer_code = "Mach1"
#This is the same method as in the Parent class "Airline_Passenger".
#The difference is instead of using password the person uses frequent_flyer_code.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_frequent_flyer_code = ("Enter your Frequent Flyer code: ")
        if  (entry_email == self.email and entry_frequent_flyer_code == self.frequent_flyer_code):
            print("Congratulations, {}, you have earned a 20% discount!".format(entry_name))
        else:
            print("Thanks for flying SpaceForce Airlines. Your miles will be added to your Frequent Flyer account.")
                    
#Child class Stratosphere Flyer
#This gives a 30% discount and asks for an additional code so the
#passenger can identify as a frequent flyer
class Stratosphere_Flyer(Airline_Passenger):
    miles_flown = 100000
    stratosphere_flyer_discount = 0.3
    stratosphere_flyer_code = "Mach2"
#This is the same method as in the Parent class "Airline_Passenger".
#The difference is instead of using password the person uses stratosphere_flyer_code.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_stratosphere_flyer_code = ("Enter your Stratosphere Flyer code: ")
        if  (entry_email == self.email and entry_stratosphere_flyer_code == self.stratosphere_flyer_code):
            print("Congratulations, {}, you have earned a 30% discount and admittance to the executive Lounge!".format(entry_name))
        else:
            print("Thanks for flying SpaceForce Airlines. Your miles will be added to your Stratosphere Flyer account.")

#THe following code invokes the method for the Airline Passenger as well as
#Frequent FLiers and Stratosphere Fliers

patron = Airline_Passenger()
patron.getLoginInfo()

frequent_flyer = Frequent_Flyer()
frequent_flyer.getLoginInfo()

stratosphere_flyer = Stratosphere_Flyer()
stratosphere_flyer.getLoginInfo()

                    
                    


    
    
    
    
