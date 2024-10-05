
class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def __str__(self) -> str:
        return f"Animal Name is {self.name}"
    
    
def main():
    dog = Animal("Bruno", 12)
    print(dog)
    

if __name__ == "__main__":
    main()