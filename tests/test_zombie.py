# tests/test_zombie.py
import pytest
from src.models.zombie import Zombie, ZombieType

class TestZombie:
    @pytest.fixture
    def basic_zombie(self):
        return Zombie(0, 8, ZombieType.BASIC)

    def test_zombie_movement(self, basic_zombie):
        initial_x = basic_zombie.x
        basic_zombie.move()
        assert basic_zombie.x < initial_x

    def test_zombie_take_damage(self, basic_zombie):
        initial_health = basic_zombie.health
        damage = 25
        basic_zombie.take_damage(damage)
        assert basic_zombie.health == initial_health - damage