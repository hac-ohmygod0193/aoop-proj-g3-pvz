"""植物卡片模型"""
from dataclasses import dataclass
import pygame
from models.plant import PlantType, PLANT_STATS
from config.settings import CardSettings, Colors

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
        self.image.fill(Colors.CARD_COLOR)
        # 名字文字
        name_font = pygame.font.Font(None, 13)
        type_text = self.info.plant_type.name
        text = name_font.render(type_text, True, Colors.BLACK)
        text_x = (CardSettings.CARD_WIDTH - text.get_width()) // 2
        self.image.blit(text, (text_x, 5))
        
        # 添加文字顯示費用
        cost_font = pygame.font.Font(None, 24)
        cost_text = cost_font.render(str(self.info.cost), True, Colors.BLACK)
        cost_x = (CardSettings.CARD_WIDTH - cost_text.get_width()) // 2
        cost_y = CardSettings.CARD_HEIGHT - 20
        self.image.blit(cost_text, (cost_x, cost_y))
        

    def update(self, current_time: int) -> None:
        """更新卡片狀態"""
        if self.is_cooling_down:
            if current_time - self.last_used_time >= self.info.cooldown * 1000:
                self.is_cooling_down = False

    def use(self, current_time: int) -> None:
        """使用卡片"""
        self.is_cooling_down = True
        self.last_used_time = current_time

    def draw(self, surface: pygame.Surface, position: tuple[int, int], is_enough_sun) -> None:
        """繪製卡片"""
        x, y = position
        # 繪製卡片背景
        surface.blit(self.image, (x, y))
        
         # 如果正在冷卻中，顯示灰色遮罩
        if self.is_cooling_down:
            # 計算冷卻進度
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.last_used_time
            cooldown_duration = self.info.cooldown * 1000  # 轉換為毫秒
            cooldown_progress = min(elapsed_time / cooldown_duration, 1)  # 計算冷卻進度，最大為 1

            # 根據冷卻進度，計算遮罩的高度
            mask_height = CardSettings.CARD_HEIGHT * (1 - cooldown_progress)
            
            # 創建一個新的遮罩 surface
            mask = pygame.Surface((CardSettings.CARD_WIDTH, mask_height))
            mask.fill(Colors.GRAY)  # 灰色遮罩
            mask.set_alpha(200)  # 半透明
            surface.blit(mask, (x, y))  # 繪製遮罩
            
        # 如果買不起，顯示灰色遮罩
        if not is_enough_sun:
            mask = pygame.Surface((CardSettings.CARD_WIDTH, CardSettings.CARD_HEIGHT))
            mask.fill(Colors.BLACK)
            mask.set_alpha(80)
            surface.blit(mask, (x, y))
            
        # 如果被選中，繪製選中框
        if self.is_selected:
            pygame.draw.rect(surface, (255, 255, 0), (x-2, y-2, CardSettings.CARD_WIDTH+4, CardSettings.CARD_HEIGHT+4), 2)