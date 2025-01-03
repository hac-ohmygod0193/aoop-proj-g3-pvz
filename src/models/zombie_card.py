"""殭屍卡片"""
import pygame
from models.zombie import ZombieType
from config.settings import Colors, ZombieCardSettings

class ZombieCard:
    def __init__(self, zombie_type: ZombieType, x: int, y: int):
        self.zombie_type = zombie_type
        self.x = x
        self.y = y
        self.width = ZombieCardSettings.CARD_WIDTH
        self.height = ZombieCardSettings.CARD_HEIGHT
        self.cost = ZombieCardSettings.COSTS[self.zombie_type.name]
        self.cooldown = ZombieCardSettings.COOLDOWNS[self.zombie_type.name]
        self.last_used = 0
        self.is_selected = False

    def is_ready(self, current_time: int) -> bool:
        """檢查是否冷卻完成"""
        return current_time - self.last_used >= self.cooldown

    def use(self, current_time: int) -> None:
        """使用卡片"""
        self.last_used = current_time

    def draw(self, surface: pygame.Surface, brain_count: int) -> None:
        """繪製卡片"""
        current_time = pygame.time.get_ticks()
        
        # 決定卡片背景顏色
        if brain_count < self.cost:
            color = Colors.GRAY  # 花費不足，顯示灰色
        else:
            color = Colors.WHITE  # 花費充足，顯示白色

        if self.is_selected:
            color = Colors.YELLOW  # 被選中時顯示黃色

        # 繪製卡片背景
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        
        # 繪製邊框
        pygame.draw.rect(surface, Colors.BLACK, (self.x, self.y, self.width, self.height), 2)
        
        # 繪製殭屍類型文字
        name_font = pygame.font.Font(None, 13)
        type_text = self.zombie_type.name
        text = name_font.render(type_text, True, Colors.BLACK)
        text_x = self.x + (self.width - text.get_width()) // 2
        surface.blit(text, (text_x, self.y + 5))
        
        # 繪製花費
        cost_font = pygame.font.Font(None, 24)
        cost_text = str(self.cost)
        cost_surface = cost_font.render(cost_text, True, Colors.BLACK)
        cost_x = self.x + (self.width - cost_surface.get_width()) // 2
        
        surface.blit(cost_surface, (cost_x, self.y + self.height - 20))
        
        # 如果在冷卻中，繪製冷卻遮罩
        if not self.is_ready(current_time):
            elapsed_time = current_time - self.last_used
            cooldown_ratio = max(0, (self.cooldown - elapsed_time) / self.cooldown)
            cooldown_height = int(self.height * cooldown_ratio)
            
            if cooldown_height > 0:
                mask = pygame.Surface((self.width, cooldown_height))
                mask.fill(Colors.GRAY)
                mask.set_alpha(128)  # 半透明效果
                # 遮罩從底部往上減少
                surface.blit(mask, (self.x, self.y))
