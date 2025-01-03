"""植物模型"""
from enum import Enum, auto
from dataclasses import dataclass
import pygame
from config.settings import GridSettings, Colors, PlantSettings

class PlantType(Enum):
    """植物類型"""
    SUNFLOWER = auto()
    PEASHOOTER = auto()
    WALLNUT = auto()
    SQUASH = auto()

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
    PlantType.SQUASH: PlantStats(health=100, cost=75, attack=0, attack_speed=0),
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
        self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
        self.image.fill(Colors.PLANT_COLOR)

    def update(self, current_time: int) -> None:
        """更新植物狀態"""
        if current_time - self.last_attack_time >= self.stats.attack_speed * 1000:
            self.attack()
            self.last_attack_time = current_time
        #print(f"Plant at ({self.row}, {self.col}) is updating")

    def attack(self) -> None:
        """植物攻擊"""
        pass

    def draw(self, surface: pygame.Surface, grid_start_x: int, grid_start_y: int) -> None:
        """繪製植物"""
        x = grid_start_x + self.col * GridSettings.CELL_WIDTH + 5
        y = grid_start_y + self.row * GridSettings.CELL_HEIGHT + 5
        surface.blit(self.image, (x, y))
        
    def take_damage(self, damage: int) -> None:
        """受到傷害"""
        
        self.health -= damage
        # print(f"Plant {self.type} took {damage} damage, current health: {self.health}")
        # print(f"ROW:{self.row}, COL:{self.col}")
        if self.health <= 0:
            # 發出植物死亡事件
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT,
                {
                    'action': 'PLANT_DIED',
                    'row': self.row,
                    'col': self.col
                }
            ))

class Sunflower(Plant):
    """向日葵類"""
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.SUNFLOWER)
        self.sun_production_time = PlantSettings.SUNFLOWER_PRODUCTION_TIME
        self.last_attack_time = 0

    def update(self, current_time: int) -> None:
        """產生陽光"""
        super().update(current_time)
        if current_time - self.last_attack_time >= self.sun_production_time:
            # 計算陽光生成位置
            x = self.col * GridSettings.CELL_WIDTH + GridSettings.GRID_START_X
            y = self.row * GridSettings.CELL_HEIGHT + GridSettings.GRID_START_Y
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT, 
                {'action': 'PRODUCE_SUN', 'x': x, 'y': y}
            ))
            self.last_attack_time = current_time
    def _load_image(self):
        try:
            loaded_image = pygame.image.load('src\\images\\sunflower.png')
            # 調整圖片大小
            self.image = pygame.transform.scale(
                loaded_image,
                (GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10)
            )
        except pygame.error as e:
            self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
            self.image.fill(Colors.SUNFLOWER_COLOR)
        
class Peashooter(Plant):
    """豌豆射手類"""
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.PEASHOOTER)
        self.attack_interval = self.stats.attack_speed * 1000
        self.last_attack_time = 0

    def update(self, current_time: int) -> None:
        """更新豌豆射手狀態"""
        super().update(current_time)
        if current_time - self.last_attack_time >= self.attack_interval:
            self.attack()
            self.last_attack_time = current_time

    def attack(self) -> None:
        """發射豌豆"""
        # 計算豌豆發射的起始位置
        x = self.col * GridSettings.CELL_WIDTH + GridSettings.GRID_START_X + GridSettings.CELL_WIDTH // 3
        y = self.row * GridSettings.CELL_HEIGHT + GridSettings.GRID_START_Y + GridSettings.CELL_HEIGHT // 2
        
        # 發送發射豌豆的事件
        pygame.event.post(pygame.event.Event(
            pygame.USEREVENT,
            {
                'action': 'SHOOT_PEA',
                'damage': self.stats.attack,
                'row': self.row,
                'x': x,
                'y': y
            }
        ))
    def _load_image(self):
        try:
            loaded_image = pygame.image.load('src\\images\\peashooter.png')
            # 調整圖片大小
            self.image = pygame.transform.scale(
                loaded_image,
                (GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10)
            )
        except pygame.error as e:
            self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
            self.image.fill(Colors.PLANT_COLOR)

class Wallnut(Plant):
    """堅果牆類"""
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.WALLNUT)

    def _load_image(self) -> None:
        """加載植物圖片"""
        self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
        self.image.fill(Colors.WALLNUT_COLOR)

    def update(self, current_time: int) -> None:
        """更新堅果牆狀態"""
        super().update(current_time)

    def attack(self) -> None:
        """堅果牆無攻擊行為"""
        pass
    def _load_image(self):
        try:
            loaded_image = pygame.image.load('src\\images\\wallnut.png')
            # 調整圖片大小
            self.image = pygame.transform.scale(
                loaded_image,
                (GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10)
            )
        except pygame.error as e:
            self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
            self.image.fill(Colors.WALLNUT_COLOR)

class Squash(Plant):
    def __init__(self, row: int, col: int):
        super().__init__(row, col, PlantType.SQUASH)
        self.target_zombie = None  # 当前目标僵尸
        self.moving = False  # 是否正在移动
        self.waiting_to_disappear = False  # 是否等待消失
        self.move_duration = 2000  # 向前移动的时间（单位：毫秒）
        self.move_start_time = 0  # 移动开始的时间
        self.disappear_start_time = 0  # 开始消失的时间

    def update(self, current_time: int, zombies: list) -> None:
        """更新窩瓜状态"""
        if self.waiting_to_disappear:
            # 检查是否到达消失时间
            if current_time - self.disappear_start_time >= 1000:  # 等待1秒
                self.health = 0
                self.take_damage(self.health)  # 移除窩瓜
                self.waiting_to_disappear = False
        elif not self.moving:
            self.check_for_zombies(zombies)
        elif self.moving:
            elapsed_time = current_time - self.move_start_time
            self.move_forward(elapsed_time)
            
    def check_for_zombies(self, zombies: list) -> None:
        """检测是否有符合条件的僵尸"""
        for zombie in zombies:
            # 仅当僵尸在窩瓜的同一行，并在同一格或前方一格时，触发移动
            if zombie.row == self.row and zombie.col in {self.col, self.col + 1}:
                self.start_move(zombie)
                break

    def start_move(self, zombie) -> None:
        """开始向前移动并攻击目标僵尸"""
        self.moving = True
        self.move_start_time = pygame.time.get_ticks()
        self.target_zombie = zombie
        self.move_distance = 0 # 重置已移动的距离
        pygame.event.post(pygame.event.Event(
            pygame.USEREVENT,
            {'action': 'SQUASH_MOVE', 'row': self.row, 'col': self.col}
        ))

    def move_forward(self, elapsed_time: int) -> None:
        """窩瓜向前移動，基於經過的時間計算距離"""
        self.col += 1  # 模擬窩瓜前進一格
        self._load_image()  # 刷新植物的圖像

        # 檢查是否已經到達目標僵屍位置
        if self.target_zombie and abs(self.col - self.target_zombie.col) <= 1:
            # 直接擊殺目標僵屍
            self.target_zombie.take_damage(self.target_zombie.health)
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT,
                {'action': 'ZOMBIE_KILLED', 'zombie_id': id(self.target_zombie)}
            ))
            self.target_zombie = None  # 清空目標僵屍
            self.disappear_start_time = pygame.time.get_ticks()
            self.finish_move()
        
    def finish_move(self) -> None:
        """完成移动并进入等待消失状态"""
        self.moving = False
        self.waiting_to_disappear = True
        self.disappear_start_time = pygame.time.get_ticks()  # 记录消失开始时间
    
    def _load_image(self):
        try:
            loaded_image = pygame.image.load('src\\images\\squash.png')
            # 調整圖片大小
            self.image = pygame.transform.scale(
                loaded_image,
                (GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10)
            )
        except pygame.error as e:
            self.image = pygame.Surface((GridSettings.CELL_WIDTH - 10, GridSettings.CELL_HEIGHT - 10))
            self.image.fill(Colors.SQUASH_COLOR)


        

