class Stats:
    def __init__(self):
        # self.attack = int(input('attack'))
        # self.attack_percent = int(input('attack_percent'))
        # self.life = int(input('life'))
        # self.life_percent = int(input('life_percent'))
        # self.defense = int(input('defense'))
        # self.defense_percent = int(input('defense_percent'))
        # self.penetration = int(input('penetration'))
        # self.hit = int(input('hit'))
        # self.attack_speed = int(input('attack_speed'))
        # self.travel_speed = int(input('travel_speed'))
        # self.critical_hit = int(input('critical_hit'))
        # self.super_critical_hit = int(input('super_critical_hit'))
        # self.hyper_critical_hit = int(input('hyper_critical_hit'))
        # self.avoidance = int(input('avoidance'))
        # self.skill_attack = int(input('skill_attack'))
        # self.optional_attack = int(input('optional_attack'))
        # self.pet_attack = int(input('pet_attack'))
        # self.pattern = int(input('pattern'))
        # self.emblem_attack = int(input('emblem_attack'))
        # self.core = int(input('core'))
        # self.final_attack = int(input('final_attack'))
        self.attack = 2
        self.attack_percent = 2
        self.life = 2
        self.life_percent = 19
        self.defense = 2
        self.defense_percent = 30
        self.penetration = 2
        self.hit = 2
        self.attack_speed = 2
        self.travel_speed = 2
        self.critical_hit = 2
        self.super_critical_hit = 2
        self.hyper_critical_hit = 2
        self.avoidance = 2
        self.skill_attack = 2
        self.optional_attack = 2
        self.pet_attack = 2
        self.pattern_attack = 2
        self.emblem_attack = 2
        self.core_attack = 2
        self.final_attack = 2


class Clac(Stats):
    def __init__(self):
        super().__init__()

    def final_damage(self):
        return self.attack * self.attack_percent * self.optional_attack * self.pet_attack * self.pattern_attack * \
            self.emblem_attack * self.core_attack * self.final_attack

    def final_defense(self):
        return self.defense * self.defense_percent

    def final_critical_damage(self):
        return self.final_damage() * self.critical_hit

    def final_super_critical_damage(self):
        return self.final_critical_damage() * self.super_critical_hit

    def final_hyper_critical_damage(self):
        return self.final_super_critical_damage() * self.hyper_critical_hit

    def final_life_force(self):
        return self.life * self.life_percent







