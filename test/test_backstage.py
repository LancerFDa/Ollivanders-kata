from src.gilded_rose import Item, GildedRose


def test_crear_backstage():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    assert pas.name == "Backstage passes to a TAFKAL80ETC concert"
    assert pas.sell_in == 15
    assert pas.quality == 20


def test_to_string():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    # mimics Java print-only test, just ensure repr formatting
    print("toString() Backstage test")
    print(pas)
    assert str(pas) == "Backstage passes to a TAFKAL80ETC concert, 15, 20"


def test_update_quality_over_ten():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == 14
    assert pas.quality == 21


def test_update_quality_over_five():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == 5
    assert pas.quality == 22


def test_update_quality_over_zero():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == 4
    assert pas.quality == 23


def test_update_quality_pass_expired():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == -1
    assert pas.quality == 0


def test_quality_max_50():
    pas = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == 4
    assert pas.quality == 50

    pas = Item("Backstage passes to a TAFKAL80ETC concert", 9, 49)
    gilded = GildedRose([pas])
    gilded.update_quality()
    assert pas.sell_in == 8
    assert pas.quality == 50
