# tests/test_grid.py
import pytest
import pygame
from src.core.grid import Grid

class TestGrid:
    @pytest.fixture
    def grid(self):
        surface = pygame.Surface((800, 600))
        return Grid(surface)

    def test_get_cell_position(self, grid):
        row, col = 0, 0
        x, y = grid.get_cell_position(row, col)
        assert isinstance(x, int)
        assert isinstance(y, int)

    def test_get_cell_from_pixel(self, grid):
        # 測試點擊位置轉換為網格座標
        result = grid.get_cell_from_pixel(400, 300)
        assert result is not None
        assert len(result) == 2