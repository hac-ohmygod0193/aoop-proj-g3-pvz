"""植物模型"""
from enum import Enum, auto
from dataclasses import dataclass
import pygame
from config.settings import GridSettings

class PlantType(Enum):
    """植物類型"""
    SUNFLOWER = auto()
    PEASHOOTER = auto()
    WALLNUT = auto()

@dataclass
class PlantStats:
    """植物屬性"""
    health: int
    cost: int
    attack: int
    attack_speed: float

# 植物屬性配置
PLANT_STATS = {
    PlantType.SUNFLOWER: PlantStats(health=100, cost=50, attack=0, attack_speed=24.0),
    PlantType.PEASHOOTER: PlantStats(health=100, cost=100, attack=20, attack_speed=1.5),
    PlantType.WALLNUT: PlantStats(health=400, cost=50, attack=0, attack_speed=0),
}

class Plant:
    """植物基類"""
    def __init__(self, row: int, col: int, plant_type: PlantType):
        self.row = row
        self.col = col
        self.type = plant_type
        self._load_stats()
        self._load_image()
        self.last_attack_time = 0

    def _load_stats(self) -> None:
        """加載植物屬性"""
        self.stats = PLANT_STATS[self.type]
        self.health = self.stats.health

    def _load_image(self) -> None:
        """加載植物圖片"""
        # TODO: 替換為實際的圖片加載
        self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
        self.image.fill((0, 255, 0))  # 臨時用綠色表示

    def update(self, current_time: int) -> None:
        """更新植物狀態"""
        if current_time - self.last_attack_time >= self.stats.attack_speed * 1000:
            self.attack()
            self.last_attack_time = current_time

    def attack(self) -> None:
        """植物攻擊"""
        pass

    def draw(self, surface: pygame.Surface, grid_start_x: int, grid_start_y: int) -> None:
        """繪製植物"""
        x = grid_start_x + self.col * GridSettings.CELL_WIDTH + 5
        y = grid_start_y + self.row * GridSettings.CELL_HEIGHT + 5
        surface.blit(self.image, (x, y))

class Sunflower(Plant):
    """向日葵類"""
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.SUNFLOWER)

    def update(self, current_time: int) -> None:
        """產生陽光"""
        super().update(current_time)
        # TODO: 實現陽光產生邏輯

class Peashooter(Plant):
    """豌豆射手類"""
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.PEASHOOTER)

    def attack(self) -> None:
        """發射豌豆"""
        # TODO: 實現發射豌豆的邏輯
        pass

