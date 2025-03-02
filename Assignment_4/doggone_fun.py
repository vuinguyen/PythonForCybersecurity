# An example of how to use the Dog class and its methods

from dogs import Dog

dog1 = Dog("Rocky", 3, "Schnoodle")

dog1.get_age()
dog1.get_breed()

print(f'{dog1.name} can do a lot of things! Such as:')
dog1.bark()
dog1.fetch()
dog1.sit()
dog1.roll_over()
dog1.go_on_walk()