class Weapon:
    amount_of_bullets = 0

    def __init__(self, bullets: int):
        self.amount_of_bullets = bullets

    def shoot(self):
        if self.amount_of_bullets > 0:
            self.amount_of_bullets -= 1
            return f'shooting...'
        else:
            return f'no bullets left'

    def __repr__(self):
        return f"Remaining bullets: {self.amount_of_bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
