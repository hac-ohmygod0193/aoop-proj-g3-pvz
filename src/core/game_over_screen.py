"""遊戲結束畫面"""
import pygame
from config.settings import GameSettings, Colors

class GameOverScreen:
    def __init__(self, screen: pygame.Surface, winner: str):
        self.screen = screen
        self.winner = winner
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.is_running = True
        
        # 確認按鈕
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
        # 半透明背景
        overlay = pygame.Surface((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))

        # 勝利文字
        text = self.font_large.render(f"{self.winner} Win!", True, Colors.WHITE)
        text_rect = text.get_rect(center=(GameSettings.WINDOW_WIDTH // 2, 200))
        self.screen.blit(text, text_rect)

        # 確認按鈕
        mouse_pos = pygame.mouse.get_pos()
        button_color = Colors.BUTTON_HOVER if self.confirm_button.collidepoint(mouse_pos) else Colors.BUTTON_NORMAL
        pygame.draw.rect(self.screen, button_color, self.confirm_button)
        
        # 按鈕文字
        button_text = self.font_small.render("Back to Menu", True, Colors.BLACK)
        button_text_rect = button_text.get_rect(center=self.confirm_button.center)
        self.screen.blit(button_text, button_text_rect)

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