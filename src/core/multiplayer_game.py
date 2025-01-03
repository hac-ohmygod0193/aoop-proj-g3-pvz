"""多人遊戲模式"""
import pygame
from core.single_player_game import SinglePlayerGame
from core.multiplayer_grid import MultiplayerGrid
from core.brain_manager import BrainManager
from models.zombie import ZombieType
from models.tombstone import Tombstone
from core.multiplayer_zombie_manager import MultiplayerZombieManager
from config.settings import Colors
from ui.game_over import GameOverScreen
from core.zombie_card_manager import ZombieCardManager

class MultiPlayerGame(SinglePlayerGame):
    def __init__(self):
        super().__init__()
        self.selected_zombie_type = None
        
    def _setup_game_objects(self) -> None:
        """初始化遊戲物件"""
        super()._setup_game_objects()
        self.zombie_manager = MultiplayerZombieManager()
        self.brain_manager = BrainManager()
        self.zombie_card_manager = ZombieCardManager()
        self.grid = MultiplayerGrid(self.screen)  # 使用多人模式網格

    def _process_event(self, event: pygame.event.Event) -> None:
        """處理遊戲事件"""
        # 處理鍵盤輸入
        super()._process_event(event)

        if event.type == pygame.QUIT:
            self._quit_game()
            
        # 處理鍵盤事件
        if event.type == pygame.KEYDOWN:
            self.grid.handle_keyboard_event(event)
            # 處理殭屍放置
            if event.key == pygame.K_1:
                self.selected_zombie_type = ZombieType.NORMAL
            elif event.key == pygame.K_2:
                self.selected_zombie_type = ZombieType.CONE_HEAD
            elif event.key == pygame.K_3:
                self.selected_zombie_type = ZombieType.BUCKET_HEAD
            elif event.key == pygame.K_4:
                self.selected_zombie_type = ZombieType.TOMBSTONE
                
            card = self.zombie_card_manager.handle_key(event.key)
            if card and self.brain_manager.can_afford(card.cost):
                row, col = self.grid.get_selected_cell()
                if self.grid.is_in_zombie_zone(col):
                    self.brain_manager.spend_brain(card.cost)
                    self.zombie_manager.spawn_zombie(card.zombie_type, row, col)
                    card.use(pygame.time.get_ticks())

            elif event.type == pygame.MOUSEBUTTONDOWN:
                super()._handle_mouse_click(event.pos)
        
        if self.selected_zombie_type:
            row, col = self.grid.get_selected_cell()
            if self.grid.is_in_zombie_zone(col):
                pass
        
        if event.type == pygame.USEREVENT:
            if event.action == 'HIT_FLAG':
                self.zombie_manager.take_flag_damage(event.damage)
        
    def _update(self) -> None:
        """更新遊戲狀態"""
        super()._update()
        self.brain_manager.update(pygame.time.get_ticks())

    def _render(self) -> None:
        """渲染遊戲畫面"""
        self.screen.fill(Colors.WHITE)
        self.grid.draw()
        self.plant_manager.draw(self.screen, self.grid.start_x, self.grid.start_y)
        self.card_manager.draw(self.screen, self.sun_manager.sun_count)
        self.sun_manager.draw(self.screen)
        self.zombie_manager.draw(self.screen)
        for pea in self.projectiles:
            pea.draw(self.screen)
        self.effect_manager.draw(self.screen)
        self.brain_manager.draw(self.screen)
        self.zombie_card_manager.draw(self.screen, self.brain_manager.brain_count)
        pygame.display.flip()

    def _check_game_over(self) -> bool:
        """檢查遊戲是否結束"""
        # 檢查是否有殭屍到達底線
        for zombie in self.zombie_manager.zombies:
            if zombie.x <= self.grid.start_x:
                return True

        # 檢查殭屍方旗幟是否被摧毀
        if self.zombie_manager.is_flag_destroyed():
            return True

        return False

    def _show_game_over(self) -> bool:
        """顯示遊戲結束畫面"""
        winner = "Plants" if self.zombie_manager.is_flag_destroyed() else "Zombies"
        game_over = GameOverScreen(self.screen, winner)
        return game_over.run()