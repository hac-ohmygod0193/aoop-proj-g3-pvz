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
    CARD_START_X = 10
    CARD_START_Y = 10

class SunSettings:
    gameSettings = GameSettings()
    SUN_WIDTH = 40
    SUN_HEIGHT = 40
    SUN_VALUE = 25
    SUN_DISAPPEAR_TIME = 10000
    SUN_FALL_SPEED = 2
    SUN_COLLECT_SPEED = 10
    SUN_ICON_X = 20
    SUN_ICON_Y = gameSettings.WINDOW_HEIGHT - 50

class PlantSettings:
    SUNFLOWER_PRODUCTION_TIME = 5000

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    SUN_ICON = (255, 255, 0)
    PLANT_COLOR = (0, 255, 0)
    SUNFLOWER_COLOR = (255, 150, 0)
    CARD_COLOR = (200, 200, 200)
    BUTTON_NORMAL = (200, 200, 200)
    BUTTON_HOVER = (150, 150, 150)
