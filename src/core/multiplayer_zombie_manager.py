"""多人模式殭屍管理器"""
import pygame
from typing import List
from models.zombie import Zombie, ZombieType
from config.settings import GridSettings, Colors
from core.zombie_manager import ZombieManager

class MultiplayerZombieManager(ZombieManager):
    def __init__(self):
        super().__init__()
        self.flag_health = 1000  # 殭屍方旗幟的生命值
        self.max_flag_health = 1000
        # 覆蓋父類的一些屬性，因為我們不需要自動生成
        self.spawn_timer = 0
        self.wave_number = 0
        self.zombies_in_wave = 0
        self.zombies_spawned = 0
        self.wave_complete = False

    def spawn_zombie(self, zombie_type: ZombieType, row: int) -> None:
        """在指定行放置殭屍（覆蓋父類方法）"""
        zombie = Zombie(row, zombie_type)
        zombie.x = GridSettings.GRID_START_X + (GridSettings.COLS - 1) * GridSettings.CELL_WIDTH
        self.zombies.append(zombie)

    def update(self, current_time: int) -> None:
        """更新所有殭屍（覆蓋父類方法）"""
        # 只更新殭屍的移動和狀態，不自動生成新殭屍
        self.zombies = [zombie for zombie in self.zombies if not zombie.is_dead]
        for zombie in self.zombies:
            zombie.update(current_time)

    def draw(self, surface: pygame.Surface) -> None:
        """繪製所有殭屍和旗幟（覆蓋父類方法）"""
        super().draw(surface)  # 使用父類的殭屍繪製邏輯
        self._draw_flag_health(surface)  # 添加旗幟生命值條

    def _draw_flag_health(self, surface: pygame.Surface) -> None:
        """繪製旗幟生命值條"""
        bar_width = 200
        bar_height = 20
        x = GridSettings.GRID_START_X + (GridSettings.COLS - 3) * GridSettings.CELL_WIDTH
        y = 20

        # 背景條（紅色）
        pygame.draw.rect(surface, Colors.RED, (x, y, bar_width, bar_height))
        
        # 當前生命值條（綠色）
        current_width = int(bar_width * (self.flag_health / self.max_flag_health))
        if current_width > 0:
            pygame.draw.rect(surface, Colors.GREEN, (x, y, current_width, bar_height))

    def take_flag_damage(self, damage: int) -> None:
        """旗幟受到傷害"""
        self.flag_health -= damage

    def is_flag_destroyed(self) -> bool:
        """檢查旗幟是否被摧毀"""
        return self.flag_health <= 0

    # 以下方法從父類繼承，無需修改：
    # - check_collisions
    # - setup