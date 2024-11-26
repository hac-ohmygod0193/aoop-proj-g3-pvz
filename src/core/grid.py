"""網格系統"""
import pygame
from config.settings import GridSettings

class Grid:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self._calculate_start_position()

    def _calculate_start_position(self) -> None:
        """計算網格的起始位置，使其在視窗中居中"""
        window_width = self.surface.get_width()
        window_height = self.surface.get_height()
        
        self.start_x = (window_width - (GridSettings.CELL_WIDTH * GridSettings.COLS)) // 2
        self.start_y = (window_height - (GridSettings.CELL_HEIGHT * GridSettings.ROWS)) // 2

    def draw(self) -> None:
        """繪製網格"""
        self._draw_horizontal_lines()
        self._draw_vertical_lines()

    def _draw_horizontal_lines(self) -> None:
        """繪製水平線"""
        for row in range(GridSettings.ROWS + 1):
            start_pos = (self.start_x, self.start_y + row * GridSettings.CELL_HEIGHT)
            end_pos = (self.start_x + GridSettings.COLS * GridSettings.CELL_WIDTH,
                      self.start_y + row * GridSettings.CELL_HEIGHT)
            pygame.draw.line(self.surface, GridSettings.COLOR, start_pos, end_pos, GridSettings.LINE_WIDTH)

    def _draw_vertical_lines(self) -> None:
        """繪製垂直線"""
        for col in range(GridSettings.COLS + 1):
            start_pos = (self.start_x + col * GridSettings.CELL_WIDTH, self.start_y)
            end_pos = (self.start_x + col * GridSettings.CELL_WIDTH,
                      self.start_y + GridSettings.ROWS * GridSettings.CELL_HEIGHT)
            pygame.draw.line(self.surface, GridSettings.COLOR, start_pos, end_pos, GridSettings.LINE_WIDTH)

    def get_cell_from_pos(self, mouse_pos: tuple[int, int]) -> tuple[int, int] | None:
        """根據滑鼠位置獲取網格座標"""
        x, y = mouse_pos
        
        if not self._is_within_grid(x, y):
            return None
        
        col = (x - self.start_x) // GridSettings.CELL_WIDTH
        row = (y - self.start_y) // GridSettings.CELL_HEIGHT
        return (row, col)

    def _is_within_grid(self, x: int, y: int) -> bool:
        """檢查座標是否在網格範圍內"""
        return (self.start_x <= x <= self.start_x + GridSettings.COLS * GridSettings.CELL_WIDTH and
                self.start_y <= y <= self.start_y + GridSettings.ROWS * GridSettings.CELL_HEIGHT)