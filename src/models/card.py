"""植物卡片模型"""
from dataclasses import dataclass
import pygame
from models.plant import PlantType, PLANT_STATS
from config.settings import CardSettings

@dataclass
class CardInfo:
    """卡片信息"""
    plant_type: PlantType
    cost: int
    cooldown: float  # 冷卻時間（秒）
    image_path: str  # 圖片路徑



class PlantCard:
    """植物卡片類"""
    def __init__(self, card_info: CardInfo):
        self.info = card_info
        self.is_selected = False
        self.is_cooling_down = False
        self.last_used_time = 0
        self._load_image()

    def _load_image(self) -> None:
        """加載卡片圖片"""
        # TODO: 替換為實際圖片
        self.image = pygame.Surface((CardSettings.CARD_WIDTH, CardSettings.CARD_HEIGHT))
        self.image.fill((200, 200, 200))
        # 添加文字顯示費用
        font = pygame.font.Font(None, 24)
        cost_text = font.render(str(self.info.cost), True, (0, 0, 0))
        self.image.blit(cost_text, (5, 5))

    def update(self, current_time: int) -> None:
        """更新卡片狀態"""
        if self.is_cooling_down:
            if current_time - self.last_used_time >= self.info.cooldown * 1000:
                self.is_cooling_down = False

    def use(self, current_time: int) -> None:
        """使用卡片"""
        self.is_cooling_down = True
        self.last_used_time = current_time

    def draw(self, surface: pygame.Surface, position: tuple[int, int]) -> None:
        """繪製卡片"""
        x, y = position
        # 繪製卡片背景
        surface.blit(self.image, (x, y))
        
        # 如果正在冷卻中，顯示灰色遮罩
        if self.is_cooling_down:
            mask = pygame.Surface((CardSettings.CARD_WIDTH, CardSettings.CARD_HEIGHT))
            mask.fill((128, 128, 128))
            mask.set_alpha(128)
            surface.blit(mask, (x, y))
        
        # 如果被選中，繪製選中框
        if self.is_selected:
            pygame.draw.rect(surface, (255, 255, 0), (x-2, y-2, CardSettings.CARD_WIDTH+4, CardSettings.CARD_HEIGHT+4), 2)