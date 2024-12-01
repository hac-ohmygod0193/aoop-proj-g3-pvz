"""特效管理器"""
import pygame
from typing import List

class DamageIndicator:
    def __init__(self, damage: int, x: int, y: int, is_plant_damage: bool = False):
        self.damage = damage
        self.x = x
        self.y = y
        # 植物受傷顯示紅色並往下飄，殭屍受傷顯示綠色並往上飄
        self.color = (255, 0, 0) if is_plant_damage else (0, 255, 0)
        self.move_direction = 1 if is_plant_damage else -1  # 1表示向下，-1表示向上
        self.lifetime = 45  # 持續幾幀
        self.font = pygame.font.Font(None, 36)
        self.y_offset = 0
        self.fade = 255  # 透明度

    def update(self) -> bool:
        """更新動畫效果，返回False表示特效結束"""
        self.lifetime -= 1
        self.y_offset += (self.move_direction * 1)  # 向上或向下飄動
        self.fade = int(255 * (self.lifetime / 45))  # 根據剩餘生命週期計算透明度
        return self.lifetime > 0

    def draw(self, surface: pygame.Surface) -> None:
        """繪製傷害數字"""
        text = self.font.render(str(self.damage), True, self.color)
        # 創建一個臨時的surface來設置透明度
        alpha_surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)
        alpha_surface.fill((255, 255, 255, self.fade))
        text.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        surface.blit(text, (self.x, self.y + self.y_offset))

class EffectManager:
    """特效管理器"""
    def __init__(self):
        self.damage_indicators: List[DamageIndicator] = []

    def add_damage_indicator(self, damage: int, x: int, y: int, is_plant_damage: bool = False):
        """添加傷害數字"""
        self.damage_indicators.append(DamageIndicator(damage, x, y, is_plant_damage))

    def update(self) -> None:
        """更新所有特效"""
        # 使用列表切片創建副本進行迭代
        for indicator in self.damage_indicators[:]:
            indicator.update()
            if indicator.lifetime <= 0:
                self.damage_indicators.remove(indicator)

    def draw(self, surface: pygame.Surface) -> None:
        """繪製所有特效"""
        for indicator in self.damage_indicators:
            indicator.draw(surface)