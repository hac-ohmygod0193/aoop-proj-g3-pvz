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

    def spawn_zombie(self, zombie_type: ZombieType, row: int, col: int) -> None:
        """在指定行放置殭屍（覆蓋父類方法）"""
        zombie = Zombie(row, zombie_type)
        zombie.x = GridSettings.GRID_START_X + col * GridSettings.CELL_WIDTH
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
        """繪製旗幟生命值條（垂直方向）"""
        bar_width = 20
        bar_height = 300
        # 放在畫面最右邊，留一點邊距
        x = surface.get_width() - bar_width - 10
        y = 150  # 從上方開始

        # 繪製旗幟圖示
        
        # flag_rect = pygame.Rect(x - 5, y - 40, 30, 30)
        # pygame.draw.rect(surface, Colors.RED, flag_rect)
        loaded_image = pygame.image.load('src\\images\\flag.png')
        flag_icon = pygame.transform.scale(loaded_image, (30, 30))
        surface.blit(flag_icon, (x - 5, y - 40))
        # 繪製背景條（紅色）
        pygame.draw.rect(surface, Colors.RED, (x, y, bar_width, bar_height))
        
        # 計算當前生命值高度（從上往下減少）
        current_height = int(bar_height * (self.flag_health / self.max_flag_health))
        if current_height > 0:
            # 繪製當前生命值條（綠色）
            pygame.draw.rect(surface, Colors.GREEN, (x, y + (bar_height-current_height), bar_width, current_height))

        # 繪製邊框
        border_rect = pygame.Rect(x, y, bar_width, bar_height)
        pygame.draw.rect(surface, Colors.BLACK, border_rect, 2)

        # 繪製生命值文字
        font = pygame.font.Font(None, 24)
        health_text = font.render(f"{self.flag_health}", True, Colors.BLACK)
        text_x = x + (bar_width - health_text.get_width()) // 2
        text_y = y + bar_height + 10
        surface.blit(health_text, (text_x, text_y))

    def take_flag_damage(self, damage: int) -> None:
        """旗幟受到傷害"""
        self.flag_health -= damage

    def is_flag_destroyed(self) -> bool:
        """檢查旗幟是否被摧毀"""
        return self.flag_health <= 0

    # 以下方法從父類繼承，無需修改：
    # - check_collisions
    # - setup