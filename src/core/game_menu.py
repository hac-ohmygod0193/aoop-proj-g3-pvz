"""遊戲選單"""
import pygame
from config.settings import GameSettings, Colors
from models.game_mode import GameMode

class GameMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.selected_mode = None
        self.font = pygame.font.Font(None, 48)

    def draw_button(self, text: str, rect: pygame.Rect, is_hovered: bool) -> None:
        """繪製按鈕"""
        color = Colors.BUTTON_HOVER if is_hovered else Colors.BUTTON_NORMAL
        pygame.draw.rect(self.screen, color, rect)
        text_surface = self.font.render(text, True, Colors.BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def run(self) -> GameMode:
        """運行選單"""
        single_player_rect = pygame.Rect(200, 200, 400, 80)
        multiplayer_rect = pygame.Rect(200, 300, 400, 80)

        while self.is_running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if single_player_rect.collidepoint(mouse_pos):
                        return GameMode.SINGLE_PLAYER
                    if multiplayer_rect.collidepoint(mouse_pos):
                        return GameMode.MULTI_PLAYER

            self.screen.fill(Colors.WHITE)
            
            # 繪製按鈕
            self.draw_button(
                "Single Player", 
                single_player_rect,
                single_player_rect.collidepoint(mouse_pos)
            )
            self.draw_button(
                "Multi Player", 
                multiplayer_rect,
                multiplayer_rect.collidepoint(mouse_pos)
            )

            pygame.display.flip()
            self.clock.tick(GameSettings.FPS)