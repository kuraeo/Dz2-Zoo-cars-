class Zoo:
    all_animals = 0
    working_hours = "From 9 a.m. to 7 p.m."
    def __init__(self, animal_species, name, is_hungry, fly, swim):
        self.animal_species = animal_species
        self.name = name
        self.is_hungry = is_hungry
        self.fly = fly
        self.swim = swim
        Zoo.all_animals += 1

    def show_hungry(self):
        if self.is_hungry:
            print(f"{self.animal_species} {self.name} голодний")
        else:
            print(f"{self.animal_species} {self.name} ситий")

    def show_fly(self):
        if self.fly:
            print(f"{self.animal_species} {self.name} взлетів")
        else:
            print(f"{self.animal_species} {self.name} не може літати")

    def show_swim(self):
        if self.swim:
            print(f"{self.animal_species} {self.name} пливе")
        else:
            print(f"{self.animal_species} {self.name} не вміє плавати")

octopus = Zoo("Octopus", 'Grisha', False, False, True)
hawk = Zoo("Hawk", "Vasiliy", True, True, False )
fish = Zoo('Fish', "Aleksey", False, False, True)
bat = Zoo("Bat", "Gena", True, True, False )

octopus.show_hungry()
octopus.show_fly()
octopus.show_swim()

hawk.show_hungry()
hawk.show_fly()
hawk.show_swim()

fish.show_hungry()
fish.show_fly()
fish.show_swim()

bat.show_hungry()
bat.show_fly()
bat.show_swim()

print(f"Всього тварин у нашому зоопарку: {Zoo.all_animals}")
print(f"Ми відкриті: {Zoo.working_hours}")

