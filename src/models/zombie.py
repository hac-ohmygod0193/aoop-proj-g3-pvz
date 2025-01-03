"""殭屍模型"""
from enum import Enum, auto
from dataclasses import dataclass
import pygame
from config.settings import GridSettings
from config.settings import GameSettings
class ZombieType(Enum):
    """殭屍類型"""
    NORMAL = auto()
    CONE_HEAD = auto()
    BUCKET_HEAD = auto()
    TOMBSTONE = auto()

@dataclass
class ZombieStats:
    """殭屍屬性"""
    name: str
    health: int
    damage: int
    speed: float
    eat_speed: float  # 攻擊速度（秒）

# 殭屍屬性配置
ZOMBIE_STATS = {
    ZombieType.NORMAL: ZombieStats(
        name='normal',
        health=100,
        damage=20,
        speed=0.5,
        eat_speed=1.0
    ),
    ZombieType.CONE_HEAD: ZombieStats(
        name='cone_head',
        health=200,
        damage=20,
        speed=0.5,
        eat_speed=1.0
    ),
    ZombieType.BUCKET_HEAD: ZombieStats(
        name='bucket_head',
        health=300,
        damage=20,
        speed=0.5,
        eat_speed=1.0
    ),
    ZombieType.TOMBSTONE: ZombieStats(
        name='tombstone',
        health=1000,
        damage=0,
        speed=0,
        eat_speed=0
    )
}

class Zombie:
    """殭屍基類"""
    def __init__(self, row: int, zombie_type: ZombieType):
        self.row = row
        self.type = zombie_type
        self.x = GameSettings.WINDOW_WIDTH  # 從右側進入
        self._load_stats()
        self._load_image()
        self.is_eating = False
        self.last_attack_time = 0
        self.is_dead = False

    def _load_stats(self) -> None:
        """加載殭屍屬性"""
        self.stats = ZOMBIE_STATS[self.type]
        self.health = self.stats.health

    def _load_image(self) -> None:
        """加載殭屍圖片"""
        try:
            path = f'src\\images\\{self.stats.name}.png'
            loaded_image = pygame.image.load(path)
            # 調整圖片大小
            self.image = pygame.transform.scale(
                loaded_image,
                (GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10)
            )
        except pygame.error as e:
            self.image = pygame.Surface((30, 40))
            color = (100, 100, 100)  # 暫時用灰色表示不同殭屍
            if self.type == ZombieType.CONE_HEAD:
                color = (139, 69, 19)  # 褐色
            elif self.type == ZombieType.BUCKET_HEAD:
                color = (192, 192, 192)  # 銀色
            elif self.type == ZombieType.TOMBSTONE:
                color = (80, 0, 80)
            self.image.fill(color)

    def update(self, current_time: int) -> None:
        """更新殭屍狀態"""
        if not self.is_eating and not self.is_dead:
            self.x -= self.stats.speed

    @property
    def col(self) -> int:
        """根据僵尸的 x 坐标计算所在的列"""
        return (self.x - GridSettings.GRID_START_X) // GridSettings.CELL_WIDTH

    def take_damage(self, damage: int) -> None:
        """受到傷害"""
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True

    def attack(self, current_time: int) -> int:
        """攻擊植物"""
        if current_time - self.last_attack_time >= self.stats.eat_speed * 1000:
            self.last_attack_time = current_time
            return self.stats.damage
        return 0

    def draw(self, surface: pygame.Surface, grid_start_y: int) -> None:
        """繪製殭屍"""
        y = grid_start_y + self.row * GridSettings.CELL_HEIGHT
        surface.blit(self.image, (self.x, y+5))

    def get_rect(self) -> pygame.Rect:
        """獲取殭屍碰撞箱"""
        y = GridSettings.GRID_START_Y + self.row * GridSettings.CELL_HEIGHT
        return pygame.Rect(self.x, y, 60, 80)

