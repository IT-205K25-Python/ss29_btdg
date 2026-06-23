from __future__ import annotations
from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, base_hp):
        self.__base_hp = base_hp
        
    @property
    def base_hp(self):
        return self.__base_hp
        
    @abstractmethod
    def attack_enemy(self):
        pass
    
    def __add__(self, other: BaseCharacter):
        return self.base_hp + other.base_hp
    
class MagicalStance:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def attack_enemy(self):
        return 150.0
    
class Warrior(BaseCharacter):
    def __init__(self, strength, **kwargs):
        self.strength = strength
        
        super().__init__(**kwargs)
        
    def attack_enemy(self):
        return self.strength * 2.5
    
class Spellblade(Warrior, MagicalStance):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def attack_enemy(self):
        Warrior.attack_enemy()
        MagicalStance.attack_enemy() 
        
list = []
def inital_spellblade(list):
    base_hp = input("Nhập lượng máu kiếm sỹ: ")
    strength = input("Nhập sức mạnh của kiếm sỹ: ")
    
    spellblade = Spellblade(base_hp = base_hp, strength = strength)
    
    list.append(spellblade)
    
    print("[Thành công]: Khởi tạo nhân vật spellblade thành công")
    
    mro_names = [
        cls.__name__ for cls in type(spellblade).__mro__ if cls.__name__ not in ("ABC",)
    ]
    
    print(f"[MRO Architecture]: {mro_names}")

while True:
    print("RPG GAME CORE MENU".center(50, "="))
    print("1. Khởi tạo Ma kiếm sĩ spellblade & xem cấu trúc MRO")
    print("2. Ra lệnh tấn công & kích hoạt chiến trường (Duck Typing)")
    print("3. Thoát")
    
    choice = input("Chọn chức năng (1-3):")
    match choice:
        case '1':
            init = inital_spellblade(list)
            print(init)
        case '2':
            pass
        case '3':
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ vui lòng nhập lại")