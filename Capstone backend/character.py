class Character:
    def __init__(self, name, initiative_bonus, ac):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.initiative = 0
        self.ac = ac

    def set_initiative(self, initiative):
        self.initiative = initiative

    def __lt__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus < other.initiative_bonus
        else:
            return self.initiative < other.initiative

    def __gt__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus > self.initiative_bonus
        else:
            return self.initiative > self.initiative_bonus

    def __eq__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus == self.initiative_bonus
        else:
            return self.initiative == other.initiative




class NPC(Character):
    def __init__(self, name, initiative_bonus, ac, hp, fort, ref, will):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.ac = ac
        self.hp = hp
        self.fort = fort
        self.ref = ref
        self.will = will
        self.initiative = 0


