class Cat:

    def __init__(self, name):
        self.name = name
        self.tasty = 50
        self.activity = 40
        self.alive = True

    def to_eat(self):
        print("Time to eat!")
        self.tasty += 1
        self.activity -= 0.5

    def to_sleep(self):
        print("Time to sleep")
        self.tasty -= 3
        self.activity -= 10

    def to_play(self):
        print("Time to play")
        self.tasty -= 10
        self.activity += 11

    def is_alive(self):
        if self.tasty < 0:
            self.alive = False
        elif self.activity < 0:
            self.alive = False

    def end_day(self):
        print(f'Tasty = {self.tasty}')
        print(f'Activity = {self.activity}')
