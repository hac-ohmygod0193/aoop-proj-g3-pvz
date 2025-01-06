import pytest
from unittest.mock import MagicMock, patch
from models.game_mode import GameMode
from main import main

@pytest.fixture
def mock_game_menu():
    with patch('main.GameMenu') as mock:
        yield mock

@pytest.fixture
def mock_single_player_game():
    with patch('main.SinglePlayerGame') as mock:
        yield mock

@pytest.fixture
def mock_multi_player_game():
    with patch('main.MultiPlayerGame') as mock:
        yield mock

def test_main_exit_on_none(mock_game_menu):
    # Setup mock to return None (simulating window close)
    menu_instance = MagicMock()
    menu_instance.run.return_value = None
    mock_game_menu.return_value = menu_instance
    
    # Run main function
    main()
    
    # Assert GameMenu was created and run
    mock_game_menu.assert_called_once()
    menu_instance.run.assert_called_once()

def test_main_single_player_mode(mock_game_menu, mock_single_player_game):
    # Setup mocks
    menu_instance = MagicMock()
    menu_instance.run.side_effect = [GameMode.SINGLE_PLAYER, None]  # Return SINGLE_PLAYER first, then None to exit
    mock_game_menu.return_value = menu_instance
    
    game_instance = MagicMock()
    mock_single_player_game.return_value = game_instance
    
    # Run main function
    main()
    
    # Assert correct game mode was created and run
    mock_single_player_game.assert_called_once()
    game_instance.run.assert_called_once()

def test_main_multi_player_mode(mock_game_menu, mock_multi_player_game):
    # Setup mocks
    menu_instance = MagicMock()
    menu_instance.run.side_effect = [GameMode.MULTI_PLAYER, None]  # Return MULTI_PLAYER first, then None to exit
    mock_game_menu.return_value = menu_instance
    
    game_instance = MagicMock()
    mock_multi_player_game.return_value = game_instance
    
    # Run main function
    main()
    
    # Assert correct game mode was created and run
    mock_multi_player_game.assert_called_once()
    game_instance.run.assert_called_once()

def test_main_multiple_games(mock_game_menu, mock_single_player_game, mock_multi_player_game):
    # Setup mocks
    menu_instance = MagicMock()
    menu_instance.run.side_effect = [
        GameMode.SINGLE_PLAYER,
        GameMode.MULTI_PLAYER,
        None
    ]  # Play single player, then multiplayer, then exit
    mock_game_menu.return_value = menu_instance
    
    single_game_instance = MagicMock()
    mock_single_player_game.return_value = single_game_instance
    
    multi_game_instance = MagicMock()
    mock_multi_player_game.return_value = multi_game_instance
    
    # Run main function
    main()
    
    # Assert both game modes were created and run
    mock_single_player_game.assert_called_once()
    single_game_instance.run.assert_called_once()
    mock_multi_player_game.assert_called_once()
    multi_game_instance.run.assert_called_once()