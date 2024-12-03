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

class ZombieCardSettings:
    CARD_WIDTH = 60
    CARD_HEIGHT = 70
    START_X = 600  # 卡片起始X座標
    START_Y = 20   # 卡片起始Y座標
    SPACING = 70   # 卡片間距
    
    # 殭屍花費
    COSTS = {
        'NORMAL': 50,
        'CONE_HEAD': 75,
        'TOMBSTONE': 100
    }
    
    # 殭屍冷卻時間（毫秒）
    COOLDOWNS = {
        'NORMAL': 5000,    # 5秒
        'CONE_HEAD': 7000, # 7秒
        'TOMBSTONE': 10000 # 10秒
    }

class SunSettings:
    gameSettings = GameSettings()
    SUN_WIDTH = 40
    SUN_HEIGHT = 40
    SUN_VALUE = 25
    SUN_GENERATE_INTERVAL = 5000
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
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    SUN_ICON = (255, 255, 0)
    BRAIN_ICON = (255, 0, 255)
    PLANT_COLOR = (0, 255, 0)
    SUNFLOWER_COLOR = (255, 150, 0)
    WALLNUT_COLOR = (139, 69, 19)
    CARD_COLOR = (200, 200, 200)
    BUTTON_NORMAL = (200, 200, 200)
    BUTTON_HOVER = (150, 150, 150)
    ZONE_SEPARATOR = (255, 0, 0)  # 分隔線顏色
    CELL_HIGHLIGHT = (255, 0, 100)  # 選中格子的高亮顏色

class BrainSettings:
    gameSettings = GameSettings()
    INITIAL_BRAIN = 50
    BRAIN_GENERATE_INTERVAL = 5000  # 每10秒生成一次大腦
    BRAIN_GENERATE_AMOUNT = 25
    BRAIN_ICON_X = gameSettings.WINDOW_WIDTH - 100
    BRAIN_ICON_Y = gameSettings.WINDOW_HEIGHT - 50

class ZombieZoneSettings:
    COLS_START = 6
    COLS_END = 9
    FLAG_HEALTH = 1000  # 殭屍方旗幟的生命值

class TombstoneSettings:
    HEALTH = 200  # 墓碑生命值
    COST = 75    # 放置墓碑所需的 brain
    WIDTH = 60   # 墓碑寬度
    HEIGHT = 80  # 墓碑高度
