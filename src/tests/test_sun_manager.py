# tests/test_sun_manager.py
import pytest
from core.sun_manager import SunManager

class TestSunManager:
    @pytest.fixture
    def sun_manager(self):
        return SunManager()

    def test_initial_sun_count(self, sun_manager):
        assert sun_manager.sun_count == 50

    def test_add_sun(self, sun_manager):
        initial_sun = sun_manager.sun_count
        sun_manager.add_sun(25)
        assert sun_manager.sun_count == initial_sun + 25

    def test_spend_sun(self, sun_manager):
        initial_sun = sun_manager.sun_count
        sun_manager.spend_sun(25)
        assert sun_manager.sun_count == initial_sun - 25