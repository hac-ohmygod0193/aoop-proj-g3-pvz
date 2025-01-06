"""殭屍方資源管理器"""
import pygame
from config.settings import BrainSettings, Colors

class BrainManager:
    def __init__(self):
        self.brain_count = BrainSettings.INITIAL_BRAIN
        self.last_brain_time = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, current_time: int) -> None:
        """更新大腦資源"""
        if current_time - self.last_brain_time >= BrainSettings.BRAIN_GENERATE_INTERVAL:
            self.brain_count += BrainSettings.BRAIN_GENERATE_AMOUNT
            self.last_brain_time = current_time

    def can_afford(self, amount: int) -> bool:
        """檢查是否有足夠的大腦"""
        return self.brain_count >= amount

    def spend_brain(self, amount: int) -> bool:
        """消耗大腦"""
        if self.can_afford(amount):
            self.brain_count -= amount
            return True
        return False

    def draw(self, surface: pygame.Surface) -> None:
        """繪製大腦計數器"""
        brain_text = self.font.render(str(self.brain_count), True, Colors.BLACK)
        loaded_image = pygame.image.load('./images/brain.png')
        brain_icon = pygame.transform.scale(loaded_image, (30, 30))

        # 計算左下角位置
        icon_x = BrainSettings.BRAIN_ICON_X
        icon_y = BrainSettings.BRAIN_ICON_Y
        text_x = icon_x + 40
        text_y = icon_y + 5  # 稍微調整文字垂直位置使其居中
        
        surface.blit(brain_icon, (icon_x, icon_y))
        surface.blit(brain_text, (text_x, text_y))