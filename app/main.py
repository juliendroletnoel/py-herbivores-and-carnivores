class Animal (object):

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def __class__(cls) -> dict:
        return {{"Name": animal.name,
                 "Health": animal.health,
                 "Hidden": animal.hidden}
                for animal in Animal.alive}


class Herbivore (Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore (Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden:
            return

        if not isinstance(herbivore, Herbivore):
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            animals = [element.name for element in Animal.alive]
            index = animals.index(herbivore.name)
            Animal.alive.remove(index)
