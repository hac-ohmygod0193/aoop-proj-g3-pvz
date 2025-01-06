import pytest
import pygame
from src.models.plant import PlantType, Plant, Sunflower, Peashooter
from src.core.plant_manager import PlantManager

# 初始化 pygame，因為某些類需要它
pygame.init()

class TestPlantManager:
    @pytest.fixture
    def plant_manager(self):
        """建立 PlantManager 實例的 fixture"""
        return PlantManager()

    @pytest.fixture
    def sufficient_sun(self):
        """模擬足夠的陽光資源"""
        return 1000

    def test_add_sunflower(self, plant_manager, sufficient_sun):
        """測試添加向日葵"""
        # 安排
        row, col = 0, 0
        
        # 執行
        success = plant_manager.add_plant(row, col, PlantType.SUNFLOWER, sufficient_sun)
        
        # 斷言
        assert success == True
        assert (row, col) in plant_manager.plants
        assert isinstance(plant_manager.plants[(row, col)], Sunflower)

    def test_add_plant_to_occupied_position(self, plant_manager, sufficient_sun):
        """測試在已佔用的位置添加植物"""
        # 安排
        row, col = 0, 0
        plant_manager.add_plant(row, col, PlantType.SUNFLOWER, sufficient_sun)
        
        # 執行
        success = plant_manager.add_plant(row, col, PlantType.PEASHOOTER, sufficient_sun)
        
        # 斷言
        assert success == False
        assert isinstance(plant_manager.plants[(row, col)], Sunflower)

    def test_remove_plant(self, plant_manager, sufficient_sun):
        """測試移除植物"""
        # 安排
        row, col = 0, 0
        plant_manager.add_plant(row, col, PlantType.SUNFLOWER, sufficient_sun)
        
        # 執行
        plant_manager.remove_plant(row, col)
        
        # 斷言
        assert (row, col) not in plant_manager.plants

    def test_insufficient_sun(self, plant_manager):
        """測試陽光不足的情況"""
        # 安排
        row, col = 0, 0
        insufficient_sun = 0
        
        # 執行
        success = plant_manager.add_plant(row, col, PlantType.SUNFLOWER, insufficient_sun)
        
        # 斷言
        assert success == False
        assert (row, col) not in plant_manager.plants

    def test_can_place_plant(self, plant_manager):
        """測試檢查位置是否可以放置植物"""
        # 安排
        row, col = 0, 0
        
        # 執行
        can_place = plant_manager.can_place_plant(row, col)
        
        # 斷言
        assert can_place == True