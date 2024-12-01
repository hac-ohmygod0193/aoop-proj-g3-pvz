"""子彈模型"""
import pygame
from config.settings import GameSettings

class Pea:
    """豌豆子彈類"""
    def __init__(self, x: int, y: int, row: int, damage: int):
        self.x = x
        self.y = y
        self.row = row
        self.damage = damage
        self.speed = 5  # 豌豆移動速度
        self.radius = 10  # 豌豆半徑
        self.active = True
        
    def update(self) -> None:
        """更新豌豆位置"""
        self.x += self.speed
        # 如果豌豆超出螢幕範圍,將其設為非活動狀態
        if self.x > GameSettings.WINDOW_WIDTH:
            self.active = False
            
    def draw(self, surface: pygame.Surface) -> None:
        """繪製豌豆"""
        pygame.draw.circle(surface, (50, 200, 0), (int(self.x), int(self.y)), self.radius)
        
    def get_rect(self) -> pygame.Rect:
        """獲取豌豆的碰撞矩形"""
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                         self.radius * 2, self.radius * 2)