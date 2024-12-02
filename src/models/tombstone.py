"""墓碑模型"""
import pygame
from config.settings import TombstoneSettings, GridSettings

class Tombstone:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.health = TombstoneSettings.HEALTH
        self.max_health = TombstoneSettings.HEALTH
        self.cost = TombstoneSettings.COST
        
        # 計算墓碑在網格中的實際位置
        self.x = GridSettings.GRID_START_X + col * GridSettings.CELL_WIDTH
        self.y = GridSettings.GRID_START_Y + row * GridSettings.CELL_HEIGHT
        
        # 創建墓碑的矩形區域（用於碰撞檢測）
        self.rect = pygame.Rect(
            self.x + (GridSettings.CELL_WIDTH - TombstoneSettings.WIDTH) // 2,
            self.y + (GridSettings.CELL_HEIGHT - TombstoneSettings.HEIGHT) // 2,
            TombstoneSettings.WIDTH,
            TombstoneSettings.HEIGHT
        )

    def take_damage(self, damage: int) -> None:
        """受到傷害"""
        self.health -= damage
        
    def is_destroyed(self) -> bool:
        """檢查墓碑是否被摧毀"""
        return self.health <= 0

    def draw(self, surface: pygame.Surface) -> None:
        """繪製墓碑"""
        # 繪製墓碑主體
        pygame.draw.rect(surface, (128, 128, 128), self.rect)  # 灰色墓碑
        
        # 繪製生命值條
        health_bar_width = 50
        health_bar_height = 5
        health_bar_x = self.rect.centerx - health_bar_width // 2
        health_bar_y = self.rect.y - 10
        
        # 背景條（紅色）
        pygame.draw.rect(surface, (255, 0, 0), (
            health_bar_x,
            health_bar_y,
            health_bar_width,
            health_bar_height
        ))
        
        # 當前生命值條（綠色）
        current_health_width = int(health_bar_width * (self.health / self.max_health))
        if current_health_width > 0:
            pygame.draw.rect(surface, (0, 255, 0), (
                health_bar_x,
                health_bar_y,
                current_health_width,
                health_bar_height
            ))