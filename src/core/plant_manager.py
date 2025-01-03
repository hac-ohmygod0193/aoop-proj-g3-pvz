"""植物管理器"""
from typing import Dict, Tuple
import pygame
from models.plant import Plant, Sunflower, Peashooter, Wallnut, Squash, PlantType, PLANT_STATS

class PlantManager:
    def __init__(self):
        self.plants: Dict[Tuple[int, int], Plant] = {}

    def add_plant(self, row: int, col: int, plant_type: PlantType, current_sun: int) -> bool:
        """添加植物"""
        if self.can_place_plant(row, col) and current_sun >= PLANT_STATS[plant_type].cost:
            if plant_type == PlantType.SUNFLOWER:
                plant = Sunflower(row, col)
            elif plant_type == PlantType.PEASHOOTER:
                plant = Peashooter(row, col)
            elif plant_type == PlantType.WALLNUT:
                plant = Wallnut(row, col)
            elif plant_type == PlantType.SQUASH:
                plant = Squash(row, col)
            else:
                return False

            self.plants[(row, col)] = plant
            
            #costsun
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT,
                {'action': 'COST_SUN', 'amount': PLANT_STATS[plant_type].cost}
            ))
            # print(self.plants)
            return True
        return False

    def can_place_plant(self, row: int, col: int) -> bool:
        """檢查是否可以放置植物"""
        return (row, col) not in self.plants

    def update(self, current_time: int, zombies: list) -> None:
        """更新所有植物"""
        for plant in list(self.plants.values()):
            if plant is not None:
                if isinstance(plant, Squash):
                    plant.update(current_time, zombies)
                else:
                    plant.update(current_time)

    def draw(self, surface: pygame.Surface, grid_start_x: int, grid_start_y: int) -> None:
        """繪製所有植物"""
        #print(self.plants)
        for plant in self.plants.values():
            plant.draw(surface, grid_start_x, grid_start_y)
        
    def remove_plant(self, row: int, col: int) -> None:
        """移除植物"""
        if (row, col) in self.plants:
            del self.plants[(row, col)]