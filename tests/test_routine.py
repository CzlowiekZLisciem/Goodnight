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