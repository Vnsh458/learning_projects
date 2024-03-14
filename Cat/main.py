class Cat:
    def __init__(self, name):
        self.name = name
        self.health = 0

    def feed(self, food_fount):
        if 1 <= food_fount:
            self.health += food_fount
        else:
            print("Bad master, why are you poisoning your cat?")
            self.health += food_fount

    def punish(self, hit):
        if 1 <= hit:
            self.health -= hit
        else:
            print("Are you praising her or something?")
            self.health -= hit

    def condition(self):
        if self.health > 0:
            print(f"{self.name}`s health is {self.health}")
        elif self.health == 0:
            print(f"Harry up {self.name}`s almost dead ({self.name}`s health is {self.health})")
        else:
            print(f"Late. {self.name}`s already dead ({self.name}`s health is {self.health})")


cat = Cat(input("Enter name of your cat: "))


def name_cat():

    cat.feed(int(input("Feed your cat: ")))
    cat.punish(int(input("Punish your cat, if you want of course: ")))

    if cat.health >= 0:
        cat.condition()
        question = input("Do you want continue?\n")
        if question == "yes":
            name_cat()
        else:
            print("Bye")
    else:
        cat.condition()


name_cat()
