import pytest

from mindspace.routine import Routine


def test_new_routine_is_empty():
    routine = Routine()

    assert routine.items == {}


def test_add_item():
    routine = Routine()

    routine.add_item("drink_water", "Drink a glass of water")

    assert "drink_water" in routine.items
    assert routine.items["drink_water"]["name"] == "Drink a glass of water"
    assert routine.items["drink_water"]["completed"] is False


def test_complete_item():
    routine = Routine()

    routine.add_item("stretch", "Stretch for 5 minutes")
    routine.complete_item("stretch")

    assert routine.items["stretch"]["completed"] is True


def test_cannot_complete_unknown_item():
    routine = Routine()

    with pytest.raises(ValueError):
        routine.complete_item("fly_to_the_moon")

def test_progress_calculation():
    routine = Routine()

    routine.add_item("drink_water", "Drink a glass of water")
    routine.add_item("stretch", "Stretch for 5 minutes")
    routine.add_item("brush_teeth", "Brush your teeth")
    routine.add_item("put_phone_away", "Put your phone away")

    routine.complete_item("drink_water")
    routine.complete_item("stretch")

    assert routine.get_progress() == 50

def test_empty_routine_has_zero_progress():
    routine = Routine()

    assert routine.get_progress() == 0

def test_routine_is_not_complete_with_unfinished_items():
    routine = Routine()

    routine.add_item("drink_water", "Drink a glass of water")
    routine.add_item("stretch", "Stretch for 5 minutes")

    routine.complete_item("drink_water")

    assert routine.is_complete() is False

def test_routine_is_complete_when_all_items_are_finished():
    routine = Routine()

    routine.add_item("drink_water", "Drink a glass of water")
    routine.add_item("stretch", "Stretch for 5 minutes")

    routine.complete_item("drink_water")
    routine.complete_item("stretch")

    assert routine.is_complete() is True

def test_empty_routine_is_not_complete():
    routine = Routine()

    assert routine.is_complete() is False