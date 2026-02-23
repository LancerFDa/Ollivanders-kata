from src.gilded_rose import Item, GildedRose


def test_crear_aged_brie():
    cheese = Item("Aged Brie", 2, 0)
    assert cheese.name == "Aged Brie"
    assert cheese.sell_in == 2
    assert cheese.quality == 0


def test_to_string():
    cheese = Item("Aged Brie", 2, 0)
    # the Java test just prints; we make sure __repr__ matches expected format
    print("toString() Aged Brie test:")
    print(cheese)
    assert str(cheese) == "Aged Brie, 2, 0"


def test_update_quality_brie():
    cheese = Item("Aged Brie", 2, 0)
    gilded = GildedRose([cheese])
    gilded.update_quality()
    assert cheese.sell_in == 1
    assert cheese.quality == 1


def test_update_quality_brie_expired():
    cheese = Item("Aged Brie", 0, 0)
    gilded = GildedRose([cheese])
    gilded.update_quality()
    assert cheese.sell_in == -1
    assert cheese.quality == 2


def test_quality_max_50():
    brie = Item("Aged Brie", -1, 50)
    gilded = GildedRose([brie])
    gilded.update_quality()
    assert brie.sell_in == -2
    assert brie.quality == 50

    brie = Item("Aged Brie", -1, 49)
    gilded = GildedRose([brie])
    gilded.update_quality()
    assert brie.sell_in == -2
    assert brie.quality == 50
