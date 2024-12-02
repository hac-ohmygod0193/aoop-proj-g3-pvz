"""墓碑管理器"""
import pygame
from typing import List
from models.tombstone import Tombstone

class TombstoneManager:
    def __init__(self):
        self.tombstones: List[Tombstone] = []
        self.screen: pygame.Surface = None

    def setup(self, screen: pygame.Surface) -> None:
        """設置畫面"""
        self.screen = screen

    def place_tombstone(self, row: int, col: int) -> bool:
        """放置墓碑"""
        # 檢查該位置是否已有墓碑
        for tombstone in self.tombstones:
            if tombstone.row == row and tombstone.col == col:
                return False
        
        # 放置新墓碑
        new_tombstone = Tombstone(row, col)
        self.tombstones.append(new_tombstone)
        return True

    def update(self) -> None:
        """更新墓碑狀態"""
        # 移除被摧毀的墓碑
        self.tombstones = [t for t in self.tombstones if not t.is_destroyed()]

    def draw(self, surface: pygame.Surface) -> None:
        """繪製所有墓碑"""
        for tombstone in self.tombstones:
            tombstone.draw(surface)

    def get_tombstone_at(self, row: int, col: int) -> Tombstone:
        """獲取指定位置的墓碑"""
        for tombstone in self.tombstones:
            if tombstone.row == row and tombstone.col == col:
                return tombstone
        return None

    def handle_projectile_collision(self, projectile) -> bool:
        """處理與投射物的碰撞"""
        for tombstone in self.tombstones:
            if projectile.row == tombstone.row and tombstone.rect.colliderect(projectile.get_rect()):
                tombstone.take_damage(projectile.damage)
                return True
        return False