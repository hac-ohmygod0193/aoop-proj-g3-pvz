"""遊戲結束畫面"""
import pygame
from config.settings import GameSettings, Colors
from ui.base_screen import BaseScreen

class GameOverScreen(BaseScreen):
    def __init__(self, screen: pygame.Surface, winner: str):
        super().__init__(screen)
        self.winner = winner
        
        # 初始化確認按鈕
        button_width = 200
        button_height = 50
        self.confirm_button = pygame.Rect(
            (GameSettings.WINDOW_WIDTH - button_width) // 2,
            400,
            button_width,
            button_height
        )

    def draw(self) -> None:
        """繪製結束畫面"""
        self.draw_overlay()

        # 勝利文字
        text = self.font_large.render(f"{self.winner} Win!", True, Colors.WHITE)
        text_rect = text.get_rect(center=(GameSettings.WINDOW_WIDTH // 2, 200))
        self.screen.blit(text, text_rect)

        # 確認按鈕
        self.draw_button(
            self.confirm_button,
            "Back to Menu",
            self.confirm_button.collidepoint(pygame.mouse.get_pos())
        )

    def run(self) -> bool:
        """運行結束畫面"""
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_button.collidepoint(event.pos):
                        return True

            self.draw()
            pygame.display.flip()
        
        return False 