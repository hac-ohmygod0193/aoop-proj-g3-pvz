"""遊戲配置文件"""
class GameSettings:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    FPS = 60
    TITLE = "植物守衛戰"

class GridSettings:
    ROWS = 5
    COLS = 9
    CELL_WIDTH = 80
    CELL_HEIGHT = 80
    COLOR = (150, 150, 150)
    LINE_WIDTH = 2
    gameSettings = GameSettings()
    GRID_START_X = (gameSettings.WINDOW_WIDTH - (COLS * CELL_WIDTH)) // 2
    GRID_START_Y = (gameSettings.WINDOW_HEIGHT - (ROWS * CELL_HEIGHT)) // 2

class CardSettings:
    CARD_WIDTH = 60
    CARD_HEIGHT = 70

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)