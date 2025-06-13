# src/trumpy/deck/card/suit/suit.py

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
        all(option: str = "id"): スート情報の一覧を取得する.
    """

    _SUITS = {
        1 : ("spade" , "♠"),
        2 : ("heart" , "♥"),
        3 : ("club"  , "♣"),
        4 : ("dia"   , "♦")
    } # 各スートの名称とラベルを保持する辞書

    def __init__(self , id : int):
        """
        スートクラスのコンストラクタ.

        Args:
            id (int): スートを指定する数値. 指定できる範囲は 1 <= id <= 4

        Attributes:
            _id (int): スートの数値ID.
            _name (str): スートの名称 (例: 'spade').
            _label (str): スートの記号 (例: '♠').

        Raises:
            TypeError: idにint型では無い型を指定した場合.
            ValueError: idに無効な範囲を指定した場合.
        """
        if not isinstance(id, int): raise TypeError("idに指定できるのはint型のみです.")
        if not (1 <= id <= 4): raise ValueError("idに指定できるのは 1 <= id <= 4 の範囲のみです.")
        self._id = id
        self._name = self._SUITS[id][0]
        self._label = self._SUITS[id][1]

    def __str__(self):
        """
        自身が示すスートの名称を取得する特殊メソッド.
        """
        return self._name
    
    def __repr__(self):
        """
        自身が保有するインスタンス変数を取得するメソッド.
        """
        return f"id={self._id}, name={self._name}, label={self.label}"
        
    @property
    def label(self):
        """
        自身が示すスートのラベルを取得する特殊メソッド.
        """
        return self._label
    
    @classmethod
    def all(cls, option : str = "id") -> list[int | str]:
        """
        スートの一覧を返すクラスメソッド.
        オプション引数で形式を指定する. (デフォルトはid : list[int])

        Args:
            option (str): 'id' もしくは 'i', 'name' もしくは 'n', 'label' もしくは 'l' のいずれか.

        Raises:
            TypeError: optionにstr型では無い型を指定した場合.
            ValueError: optionに無効な文字列を指定した場合.
        """
        if not isinstance(option, str): raise TypeError("optionに指定できるのはstr型のみです.")
        match option.lower():
            case "id" | "i":
                return list(cls._SUITS.keys())
            case "name" | "n":
                return [_[0] for _ in cls._SUITS.values()]
            case "label" | "l":
                return [_[1] for _ in cls._SUITS.values()]
            case _:
                raise ValueError("optionには 'id' または 'i', 'name' または 'n', 'label' または 'l' を指定してください.")
