"""遊戲選單"""
import pygame
from models.game_mode import GameMode
from config.settings import GameSettings, Colors
from ui.base_screen import BaseScreen

class GameMenu(BaseScreen):
    def __init__(self):
        self.screen = pygame.display.set_mode((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        super().__init__(self.screen)
        self.clock = pygame.time.Clock()
        
        # 初始化按鈕
        button_width = 400
        button_height = 80
        self.single_player_rect = pygame.Rect(
            (GameSettings.WINDOW_WIDTH - button_width) // 2,
            200,
            button_width,
            button_height
        )
        self.multiplayer_rect = pygame.Rect(
            (GameSettings.WINDOW_WIDTH - button_width) // 2,
            300,
            button_width,
            button_height
        )

    def run(self) -> GameMode:
        """運行選單"""
        while self.is_running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.single_player_rect.collidepoint(mouse_pos):
                        return GameMode.SINGLE_PLAYER
                    if self.multiplayer_rect.collidepoint(mouse_pos):
                        return GameMode.MULTI_PLAYER

            self.screen.fill(Colors.WHITE)
            
            # 繪製按鈕
            self.draw_button(
                self.single_player_rect,
                "Single Player",
                self.single_player_rect.collidepoint(mouse_pos)
            )
            self.draw_button(
                self.multiplayer_rect,
                "Multiplayer",
                self.multiplayer_rect.collidepoint(mouse_pos)
            )

            pygame.display.flip()
            self.clock.tick(GameSettings.FPS)