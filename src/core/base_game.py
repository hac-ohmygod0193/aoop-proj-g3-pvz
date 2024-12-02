"""遊戲基礎類"""
import pygame
from abc import ABC, abstractmethod
from config.settings import GameSettings

class BaseGame(ABC):
    def __init__(self):
        pygame.init()
        self._setup_window()
        self.clock = pygame.time.Clock()
        self.is_running = True

    def _setup_window(self) -> None:
        """設置遊戲視窗"""
        self.screen = pygame.display.set_mode((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        pygame.display.set_caption(GameSettings.TITLE)

    @abstractmethod
    def _setup_game_objects(self) -> None:
        """初始化遊戲物件"""
        pass

    @abstractmethod
    def _handle_events(self) -> None:
        """處理遊戲事件"""
        pass

    @abstractmethod
    def _update(self) -> None:
        """更新遊戲狀態"""
        pass

    @abstractmethod
    def _render(self) -> None:
        """渲染遊戲畫面"""
        pass

    def run(self) -> None:
        """遊戲主循環"""
        self._setup_game_objects()
        while self.is_running:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick(GameSettings.FPS)