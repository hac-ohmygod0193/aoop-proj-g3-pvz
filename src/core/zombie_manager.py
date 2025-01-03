"""殭屍管理器"""
import random
import pygame
from typing import List
from models.zombie import Zombie, ZombieType
from config.settings import GridSettings

class ZombieManager:
    def __init__(self):
        self.zombies: List[Zombie] = []
        self.spawn_timer = 0
        self.wave_number = 1
        self.zombies_in_wave = 5
        self.zombies_spawned = 0
        self.wave_complete = False
        self.spawn_interval = 10000  # 10秒生成一個殭屍
        self.screen: pygame.Surface = None  # 添加 screen 屬性

    def setup(self, screen: pygame.Surface) -> None:
        """設置畫面"""
        self.screen = screen

    def update(self, current_time: int) -> None:
        """更新所有殭屍"""
        # 生成新殭屍
        if (self.zombies_spawned < self.zombies_in_wave and 
            current_time - self.spawn_timer >= self.spawn_interval):
            self._spawn_zombie()
            self.spawn_timer = current_time

        # 更新現有殭屍
        self.zombies = [zombie for zombie in self.zombies if not zombie.is_dead]
        for zombie in self.zombies:
            zombie.update(current_time)

        # 檢查波次是否完成
        if (self.zombies_spawned >= self.zombies_in_wave and 
            not self.zombies):
            self.wave_complete = True

    def _spawn_zombie(self) -> None:
        """生成新殭屍"""
        row = random.randint(0, GridSettings.ROWS - 1)
        zombie_type = self._get_random_zombie_type()
        zombie = Zombie(row, zombie_type)
        self.zombies.append(zombie)
        self.zombies_spawned += 1

    def _get_random_zombie_type(self) -> ZombieType:
        """根據波次隨機選擇殭屍類型"""
        if self.wave_number < 2:
            return ZombieType.NORMAL
        elif self.wave_number < 4:
            return random.choice([ZombieType.NORMAL, ZombieType.CONE_HEAD])
        else:
            return random.choice(list(ZombieType))

    def start_new_wave(self) -> None:
        """開始新的一波"""
        self.wave_number += 1
        self.zombies_in_wave = 5 + self.wave_number * 2
        self.zombies_spawned = 0
        self.wave_complete = False
        self.spawn_interval = max(10000 - self.wave_number * 500, 3000)

    def check_collisions(self, plants: dict) -> None:
        """檢查與植物的碰撞"""
        current_time = pygame.time.get_ticks()
        for zombie in self.zombies:
            # 獲取殭屍當前所在的格子
            zombie_col = (zombie.x - GridSettings.GRID_START_X) // GridSettings.CELL_WIDTH
            
            # 檢查這個格子是否有植物
            plant = plants.get((zombie.row, zombie_col))
            # print(f"Zombie at {zombie.row}, {zombie_col} is eating {plant}")
            if plant:
                # 如果有植物，停下來攻擊
                zombie.is_eating = True
                damage = zombie.attack(current_time)
                if damage > 0:
                    plant.take_damage(damage)
                    # 發送植物受傷事件
                    pygame.event.post(pygame.event.Event(
                        pygame.USEREVENT,
                        {
                            'action': 'SHOW_DAMAGE',
                            'damage': damage,
                            'x': plant.col * GridSettings.CELL_WIDTH + GridSettings.GRID_START_X + 20,
                            'y': plant.row * GridSettings.CELL_HEIGHT + GridSettings.GRID_START_Y,
                            'is_plant_damage': True
                        }
                    ))
            else:
                # 如果沒有植物，繼續移動
                zombie.is_eating = False

    def draw(self, surface: pygame.Surface) -> None:
        """繪製所有殭屍"""
        for zombie in self.zombies:
            zombie.draw(surface, GridSettings.GRID_START_Y)