"""殭屍卡片管理器"""
import pygame
from typing import Optional
from models.zombie import ZombieType
from models.zombie_card import ZombieCard
from config.settings import ZombieCardSettings

class ZombieCardManager:
    def __init__(self):
        self.cards = []
        self._setup_cards()

    def _setup_cards(self) -> None:
        """初始化卡片"""
        x = ZombieCardSettings.START_X  # 起始x座標
        y = ZombieCardSettings.START_Y  # 起始y座標
        
        # 創建三種殭屍的卡片
        for i, zombie_type in enumerate([ZombieType.NORMAL, 
                                       ZombieType.CONE_HEAD,
                                       ZombieType.BUCKET_HEAD,
                                       ZombieType.TOMBSTONE]):
            card = ZombieCard(zombie_type, 
                            x + i * (ZombieCardSettings.CARD_WIDTH), 
                            y)
            self.cards.append(card)

    def handle_key(self, key: int) -> Optional[ZombieCard]:
        """處理按鍵輸入"""
        current_time = pygame.time.get_ticks()
        
        # 映射按鍵到卡片索引
        key_to_index = {
            pygame.K_1: 0,
            pygame.K_2: 1,
            pygame.K_3: 2,
            pygame.K_4: 3
        }
        
        if key in key_to_index:
            card = self.cards[key_to_index[key]]
            if card.is_ready(current_time):
                return card
        return None
    def update(self, current_time: int) -> None:
        pass
    def draw(self, surface: pygame.Surface, brain_count: int) -> None:
        """繪製所有卡片"""
        for card in self.cards:
            card.draw(surface, brain_count)