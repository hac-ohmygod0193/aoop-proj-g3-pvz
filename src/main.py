"""遊戲入口點"""
from ui.game_menu import GameMenu
from core.single_player_game import SinglePlayerGame
from core.multiplayer_game import MultiPlayerGame
from models.game_mode import GameMode

def main():
    while True:
        # 顯示選單
        menu = GameMenu()
        selected_mode = menu.run()
        
        if selected_mode is None:  # 用戶關閉視窗
            break
            
        if selected_mode == GameMode.SINGLE_PLAYER:
            game = SinglePlayerGame()
            game.run()
        elif selected_mode == GameMode.MULTI_PLAYER:
            game = MultiPlayerGame()
            game.run()

if __name__ == "__main__":
    main()