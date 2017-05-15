#!/usr/bin/python


class Frog(object):
    """docstring for Forg"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the forg encounters {} and {}!'.format(self,
            obstacle, obstacle.action()))


class Bug(object):

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it.'


class FrogWrod(object):

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\t------------------- Frog World -----------------------\n\t'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, objstacle):
        print('{} the Wizard battles against {} and {} !'.format(self, objstacle,
            objstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork.'

    def action(self):
        return 'kills it.'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\t------------------- Wizard World ------------------\n\t'

    def make_obstacle(self):
        return Ork()

    def make_character(self):
        return Wizard(self.player_name)


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.objstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.objstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError:
        print("Age {} is invalid, please try again...".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("what's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)

    game = FrogWrod if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
