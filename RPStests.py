import RPSmodule as RPS
import pytest

def player_names():
    RPS.PlayerOne()
    RPS.PlayerTwo()

def weapons():
    RPS.WeaponOne()
    RPS.WeaponTwo()

def test_players():
    assert player_names != int, "Failed"

def test_weapons():
    assert weapons != str, "Failed"