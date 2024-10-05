class Apollo:
    
    destination = "Moon"
    
    def fly(self):
        print("Spaceship flying...")
        
    
    def get_destination(self):
        print("Destination is: ", self.destination)
        


objFirst = Apollo()

objSecond = Apollo()

objFirst.destination = "Mars"

objFirst.fly()

objFirst.get_destination()


objSecond.fly()

objSecond.get_destination()
        
        
    