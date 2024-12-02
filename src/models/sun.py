"""陽光模型"""
import random
import pygame
from config.settings import GameSettings, SunSettings

class Sun:
    """陽光類"""
    def __init__(self, x: int, y: int, target_y: int = None):
        self.x = x
        self.y = y
        self.target_y = target_y
        self.value = SunSettings.SUN_VALUE  # 陽光值
        self.collected = False
        self.falling = target_y is not None
        self.disappear_time = pygame.time.get_ticks() + SunSettings.SUN_DISAPPEAR_TIME  # 10秒後消失
        self._init_animation()

    def _init_animation(self) -> None:
        """初始化陽光動畫"""
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))  # 暫時用黃色圓形代替
        pygame.draw.circle(self.image, (255, 200, 0), (20, 20), 20)
        self.image.set_alpha(200)
        
        # 掉落速度
        self.fall_speed = SunSettings.SUN_FALL_SPEED
        # 收集動畫的目標位置（陽光計數器的位置）
        self.collect_target = (SunSettings.SUN_ICON_X, SunSettings.SUN_ICON_Y)  # 調整到你的UI位置
        self.collect_speed = SunSettings.SUN_COLLECT_SPEED

    def update(self, current_time: int) -> bool:
        """更新陽光狀態"""
        if self.collected:
            # 移動到收集位置
            dx = self.collect_target[0] - self.x
            dy = self.collect_target[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            
            if distance < self.collect_speed:
                return True  # 完成收集
            
            self.x += dx / distance * self.collect_speed
            self.y += dy / distance * self.collect_speed
        elif self.falling:
            if self.y < self.target_y:
                self.y += self.fall_speed
            
        return current_time > self.disappear_time

    def collect(self) -> None:
        """收集陽光"""
        self.collected = True

    def draw(self, surface: pygame.Surface) -> None:
        """繪製陽光"""
        surface.blit(self.image, (self.x, self.y))

    def is_clicked(self, pos: tuple[int, int]) -> bool:
        """檢查是否被點擊"""
        x, y = pos
        return (self.x <= x <= self.x + 40 and 
                self.y <= y <= self.y + 40 and 
                not self.collected)