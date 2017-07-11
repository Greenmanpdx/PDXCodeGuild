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
    def __init__(self, name, cr, xp, alignment, size, type, initiative_bonus, ac, ac_touch, ac_ff, hp, fort, ref, will,
                 melee, ranged, space, reach, strength, dex, con, intel, wis, cha, feats, skills, sq, environment,
                 organization, treasure, group, speed, source):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.ac = ac
        self.hp = hp
        self.fort = fort
        self.ref = ref
        self.will = will
        self.initiative = 0
        self.cr = cr
        self.xp = xp
        self.alignment = alignment
        self.size = size
        self.type = type
        self.ac_touch = ac_touch
        self.ac_ff = ac_ff
        self.melee = melee
        self.ranged = ranged
        self.space = space
        self.strength = strength
        self.dex = dex
        self.con = con
        self. intel = intel
        self.wis = wis
        self.cha = cha
        self.feats = feats
        self.skills = skills
        self.sq = sq
        self.environment = environment
        self.organization = organization
        self.treasure = treasure
        self.group = group
        self.speed = speed
        self.source = source
        self.reach = reach