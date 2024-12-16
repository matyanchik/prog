import functools
import sys
import os

def suppress_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout.close()
            sys.stdout = original_stdout
    return wrapper

def hero_manager(initial_hp=100):
    hp = initial_hp 

    def get_hp():
        return hp

    @suppress_output
    def heal(amount):
        nonlocal hp
        hp += amount
        if hp > 100:
            hp = 100
        return hp

    @suppress_output
    def take_damage(amount):
        nonlocal hp
        hp -= amount
        if hp < 0:
            hp = 0
        return hp

    return get_hp, heal, take_damage

get_hp, heal, take_damage = hero_manager()

print(f"Текущие HP: {get_hp()}")

heal(20)
print(f"Текущие HP после лечения: {get_hp()}")

take_damage(50)
print(f"Текущие HP после урона: {get_hp()}")

take_damage(100)
print(f"Текущие HP после тяжелого урона: {get_hp()}")