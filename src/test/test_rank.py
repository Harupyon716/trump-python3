# src/test/test_rank.py

from trumpy import Rank

import pytest


def test_rank_constructor():
    rank_1 = Rank(1)
    assert isinstance(rank_1, Rank)

    rank_4 = Rank(4)
    assert isinstance(rank_4, Rank)

    rank_10 = Rank(10)
    assert isinstance(rank_10, Rank)

    rank_13 = Rank(13)
    assert isinstance(rank_13, Rank)

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Rank("tree")

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Rank("Q")

    with pytest.raises(TypeError, match = "無効な型<class 'str'>を検出しました."):
        Rank("11")

    with pytest.raises(TypeError, match = "無効な型<class 'float'>を検出しました."):
        Rank(6.0)
    
    with pytest.raises(ValueError, match = "無効な値0を検出しました."):
        Rank(0)

    with pytest.raises(ValueError, match = "無効な値14を検出しました."):
        Rank(14)

    with pytest.raises(ValueError, match = "無効な値-13を検出しました."):
        Rank(-13)

    with pytest.raises(AttributeError, match = "ランククラスのインスタンス変数_idを変更することは出来ません."):
        rank_1._id = 2

    with pytest.raises(AttributeError, match = "ランククラスのインスタンス変数_nameを変更することは出来ません."):
        rank_1._name = "four"

    with pytest.raises(AttributeError, match = "ランククラスのインスタンス変数_labelを変更することは出来ません."):
        rank_1._label = "10"

    with pytest.raises(AttributeError, match = "ランククラスに新たなインスタンス変数scoreを定義することは出来ません."):
        rank_1.score = 4


def test_rank_str():
    rank_ace = Rank(1)
    assert str(rank_ace) == "ace"

    rank_ten = Rank(10)
    assert str(rank_ten) == "ten"

    rank_jack = Rank(11)
    assert str(rank_jack) == "jack"

    rank_king = Rank(13)
    assert str(rank_king) == "king"


def test_rank_repr():
    rank_ace = Rank(1)
    assert repr(rank_ace) == "Rank(id=1, name='ace', label='A')"

    rank_eight = Rank(8)
    assert repr(rank_eight) == "Rank(id=8, name='eight', label='8')"

    rank_queen = Rank(12)
    assert repr(rank_queen) == "Rank(id=12, name='queen', label='Q')"

    rank_king = Rank(13)
    assert repr(rank_king) == "Rank(id=13, name='king', label='K')"


def test_rank_eq():
    class NotRank_eqFalse:
        def __init__(self, id):
            self._id = id


    class NotRank_eqTrue:
        def __init__(self, id):
            self._id = id

        def __eq__(self, other : Rank):
            return self._id == other.id
        
    
    class extRank(Rank):
        pass

    target = Rank(13)

    rank13 = Rank(13)

    not_rank_eq_false = NotRank_eqFalse(13)


def test_rank_hash():
    pass


def test_rank_id():
    pass


def test_rank_name():
    pass


def test_rank_label():
    pass


def test_rank_all():
    pass


def test_rank_dict():
    pass


def test_rank_json():
    pass

