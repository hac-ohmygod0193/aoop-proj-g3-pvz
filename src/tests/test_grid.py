# tests/test_grid.py
import pytest
import pygame
from core.grid import Grid

class TestGrid:
    @pytest.fixture
    def grid(self):
        surface = pygame.Surface((800, 600))
        return Grid(surface)
    

# tests/test_grid.py
import pytest
import pygame
from core.grid import Grid

class TestGrid:
    @pytest.fixture
    def grid(self):
        surface = pygame.Surface((800, 600))
        return Grid(surface)
    def test_get_cell_from_pos(self, grid):
        # Test valid position within the grid
        result = grid.get_cell_from_pos((400, 300))
        assert result is not None
        assert len(result) == 2

        # Test position outside the grid
        result = grid.get_cell_from_pos((900, 700))
        assert result is None