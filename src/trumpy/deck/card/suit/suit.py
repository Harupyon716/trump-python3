# src/trumpy/deck/card/suit/suit.py

from __future__ import annotations
import json

class Suit:
    """
    トランプのスート (♠♥♣♦) を管理するクラス.

    Attributes:
        _id (int): スートを識別する数値 (1〜4).
        _name (str): スートの英語名.
        _label (str): スートの記号.

    Class Attributes:
        _SUITS (dict[int, tuple[str, str]]): 各スートの定義情報.

    Methods:
        all(option: str = "suit"): スート情報の一覧を取得する.
    """

    __ATTERS : tuple[str] = ("_id", "_name", "_label")

    _SUITS : dict[int , dict[str , str]] = {
        1 : {"name" : "spade" , "label" : "♠"},
        2 : {"name" : "heart" , "label" : "♥"},
        3 : {"name" : "club"  , "label" : "♣"},
        4 : {"name" : "dia"   , "label" : "♦"}
    } # 各スートの名称とラベルを保持する辞書

    __slots__ = __ATTERS

    def __init__(self , id : int) -> None:
        """
        スートクラスのコンストラクタ.

        Args:
            id (int): スートを指定する数値. 指定できる範囲は 1 <= id <= 4

        Attributes:
            _id (int): スートの番号.
            _name (str): スートの名称 (例: 'spade').
            _label (str): スートの記号 (例: '♠').

        Raises:
            TypeError: idにint型では無い型を指定した場合.
            ValueError: idに無効な範囲の値を指定した場合.
        """
        # 例外処理
        if not isinstance(id, int): raise TypeError(f"無効な型{type(id)}を検出しました.\nidに指定できるのはint型のみです.")
        if not (1 <= id <= 4): raise ValueError(f"無効な値{id}を検出しました.\nidに指定できるのは 1 <= id <= 4 の範囲のみです.")

        # インスタンス変数の初期化
        super().__setattr__("_id", id)
        super().__setattr__("_name", self._SUITS[id]["name"])
        super().__setattr__("_label", self._SUITS[id]["label"])

    def __setattr__(self, name, value) -> None:
        if name in __class__.__ATTERS:
            if hasattr(self, name):
                raise AttributeError(f"スートクラスのインスタンス変数{name}を変更することは出来ません.\nイミュータブルなオブジェクトです.")
        
        else:
            raise AttributeError(f"スートクラスに新たなインスタンス変数{name}を定義することは出来ません.")
        
        super().__setattr__(name, value)

    def __str__(self) -> str:
        """
        自身が示すスートの名称を取得する特殊メソッド.
        """
        return self._name
    
    def __repr__(self) -> str:
        """
        自身が保有するインスタンス変数を取得する特殊メソッド.
        """
        return f"Suit(id={self._id}, name='{self._name}', label='{self._label}')"
    
    def __eq__(self, other : Suit) -> bool:
        """
        自身と他のスートと等価演算の結果を取得する特殊メソッド.
        """
        # スートクラスと比較した場合
        if isinstance(other, Suit):
            return self._id == other.id
        
        # スートクラス以外と比較した場合
        return NotImplemented
    
    def __hash__(self) -> int:
        """
        自身のハッシュ値を取得する特殊メソッド.
        """
        return hash(self._id)
        
    @property
    def id(self) -> int:
        """
        自身が示すスートの番号を取得するメソッド.
        """
        return self._id

    @property
    def name(self) -> str:
        """
        自身が示すスートのラベルを取得するメソッド.
        """
        return self._name

    @property
    def label(self) -> str:
        """
        自身が示すスートのラベルを取得するメソッド.
        """
        return self._label
    
    @classmethod
    def all(cls, option : str = "suit") -> list[Suit] | list[int] | list[str]:
        """
        スートの一覧を返すクラスメソッド.
        オプション引数で形式を指定する. (デフォルトはid : list[int])

        Args:
            option (str): 'suit'もしくは's', 'id' もしくは 'i', 'name' もしくは 'n', 'label' もしくは 'l' のいずれか.

        Raises:
            TypeError: optionにstr型では無い型を指定した場合.
            ValueError: optionに無効な文字列を指定した場合.
        """
        # 無効なオプションの例外
        if not isinstance(option, str): raise TypeError(f"無効な型{type(option)}を検出しました.\noptionに指定できるのはstr型のみです.")
        
        match option.lower():
            # スートのインスタンス全種を格納したリスト
            case "suit" | "s":
                return [Suit(_) for _ in range(1, 5)]
            # スートの番号全種を格納したリスト
            case "id" | "i":
                return list(cls._SUITS.keys())
            # スートの名称全種を格納したリスト
            case "name" | "n":
                return [_["name"] for _ in cls._SUITS.values()]
            # スートの記号全種を格納したリスト
            case "label" | "l":
                return [_["label"] for _ in cls._SUITS.values()]
            # 無効なオプションの例外
            case _:
                raise ValueError(f"無効な値{option}を検出しました.\noptionには 'id' または 'i', 'name' または 'n', 'label' または 'l' を指定してください.")

    def to_dict(self) -> dict[str , int | str]:
        """
        辞書を取得するためのシリアライザ.
        """
        return {
            "id" : self.id,
            "name" : self.name,
            "label" : self.label
        }
    
    def to_json(self) -> str:
        """
        json形式の文字列を取得するシリアライザ
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)
