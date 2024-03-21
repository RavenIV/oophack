import random

MIN_HP = 80
MAX_HP = 100
MIN_ATTACK = 50
MAX_ATTACK = 90
MIN_DEFENSE = 0.1
MAX_DEFENSE = 0.4
PERSONS_NUM = 4


class Thing:
    """Класс вещи бойца."""
    def __init__(self, name, defense, attack, health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.health = health


class Person:
    """Базовый класс бойца."""
    def __init__(self, name, defense, attack, health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.health = health

    def set_things(self, things):
        for thing in things:
            self.defense += thing.defense
            self.attack += thing.attack
            self.health += thing.health

    def take_a_hit(self, attacker):
        damage = int(attacker.attack - attacker.attack * self.defense)
        self.health -= damage
        return damage

    def __str__(self):
        return f"Боец {self.name} ({self.health} HP)"


class Paladin(Person):
    """Класс паладина."""

    def __init__(self, name, defense, attack, health):
        super().__init__(name, defense, attack, health)
        self.health *= 2
        self.defense *= 2


class Warrior(Person):
    """Класс воина."""

    def __init__(self, name, defense, attack, health):
        super().__init__(name, defense, attack, health)
        self.attack *= 2


def create_things():
    """Создание вещей."""
    names = [
        'Ring', 'Sword', 'Shield', 'Knife', 'Bow', 
        'Axe', 'Ring2', 'Sword3', 'Dagger', 'Shield2'
    ]
    things = []

    for i in range(len(names)):
        name = random.choice(names)
        defense = random.uniform(0.01, 0.1)
        attack = random.randint(1, 10)
        health = random.randint(1, 10)
        things.append(Thing(name, defense, attack, health))

    return things


def create_persons():
    """Создание персонажей."""
    names = [
        'Nick',
        'Legolas',
        'Gimli',
        'Aragorn',
        'Gloin',
        'Elrond',
        'Galadriel',
        'Durin',
        'Sauron',
        'Pippin',
        'Frodo',
        'Saruman',
        'Theoden',
        'Gandalf',
        'Bilbo',
        'Thorin',
        'Gollum',
        'Kili',
        'Balin',
        'Fili',
    ]
    persons = []

    for i in range(PERSONS_NUM):
        name = random.choice(names)
        names.remove(name)
        defense = random.uniform(MIN_DEFENSE, MAX_DEFENSE)
        health = random.randint(MIN_HP, MAX_HP)
        attack = random.randint(MIN_ATTACK, MAX_ATTACK)
        persons.append(
            random.choice(
               [Person, Paladin, Warrior]
            )(name, defense, attack, health)
        )

    for person in persons:
        person.set_things(random.sample(create_things(), random.randint(1, 4)))

    return persons


def arena(persons):
    """Запуск игры."""
    while len(persons) > 1:
        couple = random.sample(persons, 2)
        defender = couple[0]
        attacker = couple[1]

        print("Выбраны бойцы:", defender, attacker)

        while True:
            damage = defender.take_a_hit(attacker)
            print(f'{attacker} наносит {damage} ед. урона по {defender}')
            if defender.health <= 0:
                persons.remove(defender)
                break
            damage = attacker.take_a_hit(defender)
            print(f'{defender} наносит {damage} ед. урона по {attacker}')
            if attacker.health <= 0:
                persons.remove(attacker)
                break

    return print(f'Победил {persons[0].name}')


if __name__ == '__main__':
    arena(create_persons())
