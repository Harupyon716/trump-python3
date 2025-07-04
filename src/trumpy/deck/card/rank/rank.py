# src/trumpy/deck/card/rank

from __future__ import annotations
import json

class Rank:
    """
    トランプのランク (A～K) を管理するクラス.

    Attributes:
        _id (int): ランクを識別する数値 (1〜13).
        _name (str): ランクの英語名.
        _label (str): ランクの記号.

    Class Attributes:
        _RANKS (dict[int, tuple[str, str]]): 各ランクの定義情報.

    Methods:
        all(option: str = "rank"): ランク情報の一覧を取得する.
    """

    __ATTRS : tuple[str] = ("_id", "_name", "_label")

    _RANKS : dict[int , dict[str , str]]= {
        1  : {"name" : "ace"   , "label" : "A" },
        2  : {"name" : "two"   , "label" : "2" },
        3  : {"name" : "three" , "label" : "3" },
        4  : {"name" : "four"  , "label" : "4" },
        5  : {"name" : "five"  , "label" : "5" },
        6  : {"name" : "six"   , "label" : "6" },
        7  : {"name" : "seven" , "label" : "7" },
        8  : {"name" : "eight" , "label" : "8" },
        9  : {"name" : "nine"  , "label" : "9" },
        10 : {"name" : "ten"   , "label" : "10"},
        11 : {"name" : "jack"  , "label" : "J" },
        12 : {"name" : "queen" , "label" : "Q" },
        13 : {"name" : "king"  , "label" : "K" }
    }

    __slots__ = __ATTRS

    def __init__(self, id : int) -> None:
        """
        ランククラスのコンストラクタ.

        Args:
            id (int): ランクを指定する数値. 指定できる範囲は 1 <= id <= 13

        Attributes:
            _id (int): ランクの番号.
            _name (str): ランクの名称 (例: 'ace').
            _label (str): ランクの記号 (例: 'A').

        Raises:
            TypeError: idにint型では無い型を指定した場合.
            ValueError: idに無効な範囲の値を指定した場合.
        """
        # 例外処理
        if not isinstance(id, int): raise TypeError(f"無効な型{type(id)}を検出しました.\nidに指定できるのはint型のみです.")
        if not (1 <= id <= 13): raise ValueError(f"無効な値{id}を検出しました.\nidに指定できるのは 1 <= id <= 13 の範囲のみです.")

        # インスタンス変数の初期化
        super().__setattr__("_id", id)
        super().__setattr__("_name", self._RANKS[id]["name"])
        super().__setattr__("_label", self._RANKS[id]["label"])

    def __setattr__(self, name, value) -> None:
        if name in __class__.__ATTRS:
            if hasattr(self, name):
                raise AttributeError(f"ランククラスのインスタンス変数{name}を変更することは出来ません.\nイミュータブルなオブジェクトです.")
        else:
            raise AttributeError(f"ランククラスに新たなインスタンス変数{name}を定義することは出来ません.")
        
        super().__setattr__(name, value)

    def __str__(self) -> str:
        """
        自身が示すランクの名称を取得する特殊メソッド.
        """
        return self._name

    def __repr__(self) -> str:
        """
        自身が保有するインスタンス変数を取得する特殊メソッド.
        """
        return f"Rank(id={self._id}, name='{self._name}', label='{self._label}')"
    
    def __eq__(self, other : Rank) -> bool:
        """
        自身と他のランクと等価演算の結果を取得する特殊メソッド.
        """
        # ランククラスと比較した場合
        if isinstance(other, Rank):
            return self._id == other.id
        
        return NotImplemented        
    
    def __hash__(self) -> int:
        """
        自身のハッシュ値を取得する特殊メソッド.
        """
        return hash(self._id)

    @property
    def id(self) -> int:
        """
        自身が示すランクの番号を取得するメソッド.
        """
        return self._id
    
    @property
    def name(self) -> str:
        """
        自身が示すランクの名称を取得するメソッド.
        """
        return self._name
    
    @property
    def label(self) -> str:
        """
        自身が示すランクのラベルを取得するメソッド.
        """
        return self._label
    
    @classmethod
    def all(cls, option : str = "rank") -> list[Rank] | list[int] | list[str]:
        """
        ランクの一覧を返すクラスメソッド.
        オプション引数で形式を指定する. (デフォルトはid : list[int])

        Args:
            option (str): 'rank'もしくは'r', 'id' もしくは 'i', 'name' もしくは 'n', 'label' もしくは 'l' のいずれか.

        Raises:
            TypeError: optionにstr型では無い型を指定した場合.
            ValueError: optionに無効な文字列を指定した場合.
        """
        # 無効なオプションの例外
        if not isinstance(option, str): raise TypeError(f"無効な型{type(option)}を検出しました.\noptionに指定できるのはstr型のみです.")

        match(option):
            # ランクのインスタンス全種を格納したリスト
            case "rank" | "r":
                return [Rank(_) for _ in range(1, 14)]
            # ランクの番号全種を格納したリスト
            case "id" | "i":
                return list(cls._RANKS.keys())
            # ランクの名称全種を格納したリスト
            case "name" | "n":
                return [_["name"] for _ in cls._RANKS.values()]
            # ランクの記号全種を格納したリスト
            case "label" | "l":
                return [_["label"] for _ in cls._RANKS.values()]
            # 無効なオプションの例外
            case _:
                raise ValueError(f"無効な値{option}を検出しました.\noptionには 'id' または 'i', 'name' または 'n', 'label' または 'l' を指定してください.")
            
    def to_dict(self) -> dict[str , str | int]:
        """
        辞書を取得するためのシリアライザ.
        """
        return {
            "type" : self.__class__.__name__,
            "id" : self._id,
            "name" : self._name,
            "label" :self._label
        }
    
    def to_json(self) -> str:
        """
        json形式の文字列を取得するシリアライザ
        """
        return json.dumps(self.to_dict(), ensure_ascii = False)

