"""卡片管理器"""
from typing import List, Optional
import pygame
from models.card import PlantCard, CardInfo
from models.plant import PlantType

class CardManager:
    def __init__(self):
        self._init_cards()
        self.selected_card: Optional[PlantCard] = None

    def _init_cards(self) -> None:
        """初始化卡片"""
        self.cards: List[PlantCard] = [
            PlantCard(CardInfo(
                plant_type=PlantType.SUNFLOWER,
                cost=50,
                cooldown=7.5,
                image_path="sunflower.png"
            )),
            PlantCard(CardInfo(
                plant_type=PlantType.PEASHOOTER,
                cost=100,
                cooldown=7.5,
                image_path="peashooter.png"
            ))
        ]

    def handle_click(self, mouse_pos: tuple[int, int]) -> Optional[PlantType]:
        """處理點擊事件"""
        x, y = mouse_pos
        card_y = 10  # 卡片起始y座標
        
        for i, card in enumerate(self.cards):
            card_x = 10 + i * 80  # 卡片x座標
            
            if (card_x <= x <= card_x + 70 and 
                card_y <= y <= card_y + 90 and 
                not card.is_cooling_down):
                
                # 取消之前的選擇
                if self.selected_card:
                    self.selected_card.is_selected = False
                
                # 設置新的選擇
                card.is_selected = True
                self.selected_card = card
                return card.info.plant_type
        
        return None

    def use_card(self, plant_type: PlantType, current_time: int) -> None:
        """使用卡片"""
        for card in self.cards:
            if card.info.plant_type == plant_type:
                card.use(current_time)
                card.is_selected = False
                self.selected_card = None
                break

    def update(self, current_time: int) -> None:
        """更新所有卡片"""
        for card in self.cards:
            card.update(current_time)

    def draw(self, surface: pygame.Surface) -> None:
        """繪製所有卡片"""
        for i, card in enumerate(self.cards):
            card.draw(surface, (10 + i * 80, 10))