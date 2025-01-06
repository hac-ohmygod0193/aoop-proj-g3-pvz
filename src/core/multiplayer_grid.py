"""多人遊戲網格系統"""
import pygame
from core.grid import Grid
from config.settings import GridSettings, Colors

class MultiplayerGrid(Grid):
    def __init__(self, surface: pygame.Surface):
        super().__init__(surface)
        self.plant_zone = range(6)  # 0-5 列為植物區
        self.zombie_zone = range(6, 9)  # 6-8 列為殭屍區
        self.selected_cell = (0, 6)  # 用於殭屍方的選擇格子

    def is_in_plant_zone(self, col: int) -> bool:
        """檢查是否在植物區域"""
        return col in self.plant_zone

    def is_in_zombie_zone(self, col: int) -> bool:
        """檢查是否在殭屍區域"""
        return col in self.zombie_zone

    def draw(self) -> None:
        """繪製網格"""
        super().draw()  # 繪製基本網格
        
        # 繪製分隔線
        separator_x = self.start_x + 6 * GridSettings.CELL_WIDTH
        start_pos = (separator_x, self.start_y)
        end_pos = (separator_x, self.start_y + GridSettings.ROWS * GridSettings.CELL_HEIGHT)
        pygame.draw.line(self.surface, Colors.ZONE_SEPARATOR, start_pos, end_pos, 4)

        # 如果有選中的格子，繪製高亮
        if self.selected_cell:
            row, col = self.selected_cell
            self.highlight_selected_cell(row, col)

    def highlight_selected_cell(self, row: int, col: int) -> None:
        """高亮顯示選中的格子"""
        rect = pygame.Rect(
            self.start_x + col * GridSettings.CELL_WIDTH,
            self.start_y + row * GridSettings.CELL_HEIGHT,
            GridSettings.CELL_WIDTH,
            GridSettings.CELL_HEIGHT
        )
        pygame.draw.rect(self.surface, Colors.CELL_HIGHLIGHT, rect, 3)

    def handle_keyboard_event(self, event: pygame.event.Event) -> None:
        """處理鍵盤事件"""
        if not self.selected_cell:
            self.selected_cell = (0, 6)  # 預設選擇殭屍區域的第一格
            return

        if event.type == pygame.KEYDOWN:
            row, col = self.selected_cell
            
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and row > 0:
                row -= 1
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and row < GridSettings.ROWS - 1:
                row += 1
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and col > 6:
                col -= 1
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and col < GridSettings.COLS - 1:
                col += 1

            self.selected_cell = (row, col)

    def get_selected_cell(self) -> tuple[int, int]:
        """獲取當前選中的格子"""
        return self.selected_cell
