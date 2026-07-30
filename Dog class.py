class Dog:
    def __init__(self, dog_name, dog_breed, dog_age):
        self.name = dog_name
        self.breed = dog_breed
        self.age = dog_age

    def bark(self):
        print(f"{self.name} says Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

if __name__ == "__main__":
    first_dog = Dog("Buddy", "Golden Retriever", 3)
    second_dog = Dog("Max", "German Shepherd", 5)

    print(f"{first_dog.name} is {first_dog.age} years old.")
    first_dog.bark()
    first_dog.celebrate_birthday()

    print(f"\n{second_dog.name} is {second_dog.age} years old.")
    second_dog.bark()
    second_dog.celebrate_birthday()
