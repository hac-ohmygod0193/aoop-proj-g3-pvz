"""UI基礎類"""
import pygame
from config.settings import GameSettings, Colors

class BaseScreen:
    def __init__(self, screen: pygame.Surface):
        if not pygame.get_init():
            pygame.init()
        if not pygame.font.get_init():
            pygame.font.init()
            
        self.screen = screen
        self.is_running = True
        self.font_large = pygame.font.Font(None, 74)
        self.font_normal = pygame.font.Font(None, 36)

    def draw_button(self, rect: pygame.Rect, text: str, is_hovered: bool) -> None:
        """繪製按鈕"""
        color = Colors.BUTTON_HOVER if is_hovered else Colors.BUTTON_NORMAL
        pygame.draw.rect(self.screen, color, rect)
        
        text_surface = self.font_normal.render(text, True, Colors.BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_overlay(self, alpha: int = 128) -> None:
        """繪製半透明遮罩"""
        overlay = pygame.Surface((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)
        self.screen.blit(overlay, (0, 0))
