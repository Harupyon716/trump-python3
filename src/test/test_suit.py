# src/test/test_suit.py

from trumpy import Suit

import pytest


def test_suit_constructer():
    suit_1 = Suit(1)
    assert isinstance(suit_1, Suit)

    suit_4 = Suit(4)
    assert isinstance(suit_4, Suit)

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Suit("spade")

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Suit("♣")

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Suit("2")

    with pytest.raises(TypeError, match = "無効な型<class 'float'>を検出しました."):
        Suit(4.0)
    
    with pytest.raises(ValueError, match = "無効な値0を検出しました."):
        Suit(0)

    with pytest.raises(ValueError, match = "無効な値5を検出しました."):
        Suit(5)

    with pytest.raises(ValueError, match = "無効な値-3を検出しました."):
        Suit(-3)

    with pytest.raises(AttributeError, match = "スートクラスのインスタンス変数_idを変更することは出来ません."):
        suit_1._id = 2

    with pytest.raises(AttributeError, match = "スートクラスのインスタンス変数_nameを変更することは出来ません."):
        suit_1._name = "club"

    with pytest.raises(AttributeError, match = "スートクラスのインスタンス変数_labelを変更することは出来ません."):
        suit_1._label = "♦"

    with pytest.raises(AttributeError):
        suit_1.score = 10


def test_suit_str():
    suit_spade = Suit(1)
    assert str(suit_spade) == "spade"

    suit_heart = Suit(2)
    assert str(suit_heart) == "heart"

    suit_club = Suit(3)
    assert str(suit_club) == "club"

    suit_dia = Suit(4)
    assert str(suit_dia) == "dia"


def test_suit_repr():
    suit_spade = Suit(1)
    assert repr(suit_spade) == "Suit(id=1, name='spade', label='♠')"

    suit_spade = Suit(2)
    assert repr(suit_spade) == "Suit(id=2, name='heart', label='♥')"

    suit_spade = Suit(3)
    assert repr(suit_spade) == "Suit(id=3, name='club', label='♣')"

    suit_spade = Suit(4)
    assert repr(suit_spade) == "Suit(id=4, name='dia', label='♦')"


def test_suit_eq():
    class NotSuit_eqFalse:
        def __init__(self, id : int):
            self._id = id

        @property
        def id(self):
            return self._id
    
    class NotSuit_eqTrue:
        def __init__(self, id : int):
            self._id = id

        @property
        def id(self):
            return self._id
        
        def __eq__(self, other : Suit):
            return self.id == other.id
        
    class extSuit(Suit):
        pass

    target = Suit(1)

    suit1 = Suit(1)
    suit2 = Suit(2)

    not_suit_eq_false = NotSuit_eqFalse(1)
    not_suit_eq_true = NotSuit_eqTrue(1)

    ext_suit = extSuit(1)

    assert target == suit1
    assert target != suit2
    assert suit1 == target
    assert suit2 != target

    assert target != not_suit_eq_false
    assert target == not_suit_eq_true
    assert not_suit_eq_false != target
    assert not_suit_eq_true == target

    assert target == ext_suit
    assert ext_suit == target

    assert target != 1
    assert target != "spade"
    assert target != "♠"
    assert 1 != target
    assert "spade" != target
    assert "♠" != target

    assert target != None
    assert None != target

    assert target == target

def test_suit_hash():
    s1 = Suit(1)
    s2 = Suit(2)
    s3 = Suit(1)

    d = {s1: "spade", s2: "heart"}
    assert d[s3] == "spade"


def test_suit_id():
    suit_1 = Suit(1)
    assert suit_1.id == 1

    suit_2 =Suit(2)
    assert suit_2.id == 2

    suit_3 =Suit(3)
    assert suit_3.id == 3

    suit_4 =Suit(4)
    assert suit_4.id == 4


def test_suit_name():
    suit_spade = Suit(1)
    assert suit_spade.name == "spade"

    suit_heart = Suit(2)
    assert suit_heart.name == "heart"

    suit_club = Suit(3)
    assert suit_club.name == "club"

    suit_dia = Suit(4)
    assert suit_dia.name == "dia"


def test_suit_label():
    suit_spade = Suit(1)
    assert suit_spade.label == "♠"

    suit_heart = Suit(2)
    assert suit_heart.label == "♥"

    suit_club = Suit(3)
    assert suit_club.label == "♣"

    suit_dia = Suit(4)
    assert suit_dia.label == "♦"


def test_all():
    assert Suit.all() == [Suit(1), Suit(2), Suit(3), Suit(4)]
    assert Suit.all("suit") == [Suit(1), Suit(2), Suit(3), Suit(4)]
    assert Suit.all("s") == [Suit(1), Suit(2), Suit(3), Suit(4)]

    assert Suit.all("id") == [1, 2, 3, 4]
    assert Suit.all("i") == [1, 2, 3, 4]

    assert Suit.all("name") == ["spade", "heart", "club", "dia"]
    assert Suit.all("n") == ["spade", "heart", "club", "dia"]

    assert Suit.all("label") == ["♠", "♥", "♣", "♦"]
    assert Suit.all("l") == ["♠", "♥", "♣", "♦"]

    with pytest.raises(TypeError, match="無効な型<class 'int'>を検出しました."):
        Suit.all(1)

    with pytest.raises(ValueError, match="無効な値valueを検出しました."):
        Suit.all("value")


def test_suit_dict():
    suit = Suit(4)
    assert suit.to_dict() == {"id": 4, "name": "dia", "label": "♦"}


def test_suit_json():
    suit = Suit(3)
    assert suit.to_json() == '{"id": 3, "name": "club", "label": "♣"}'
