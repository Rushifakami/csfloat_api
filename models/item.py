from typing import Dict, Any, List, Optional
from .stickers import Sticker


class Item:
    __slots__ = (
        "_asset_id",
        "_def_index",
        "_paint_index",
        "_paint_seed",
        "_float_value",
        "_icon_url",
        "_d_param",
        "_is_stattrak",
        "_is_souvenir",
        "_rarity",
        "_quality",
        "_market_hash_name",
        "_low_rank",
        "_stickers",
        "_tradable",
        "_inspect_link",
        "_has_screenshot",
        "_cs2_screenshot_id",
        "_cs2_screenshot_at",
        "_is_commodity",
        "_type",
        "_rarity_name",
        "_type_name",
        "_item_name",
        "_wear_name",
        "_description",
        "_collection",
        "_badges",
        "_serialized_inspect",
        "_gs_sig"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._asset_id = data.get("asset_id")
        self._def_index = data.get("def_index")
        self._paint_index = data.get("paint_index")
        self._paint_seed = data.get("paint_seed")
        self._float_value = data.get("float_value")
        self._icon_url = data.get("icon_url")
        self._d_param = data.get("d_param")
        self._is_stattrak = data.get("is_stattrak")
        self._is_souvenir = data.get("is_souvenir")
        self._rarity = data.get("rarity")
        self._quality = data.get("quality")
        self._market_hash_name = data.get("market_hash_name")
        self._low_rank = data.get("low_rank")
        self._stickers = data.get("stickers")
        self._tradable = data.get("tradable")
        self._inspect_link = data.get("inspect_link")
        self._has_screenshot = data.get("has_screenshot")
        self._cs2_screenshot_id = data.get("cs2_screenshot_id")
        self._cs2_screenshot_at = data.get("cs2_screenshot_at")
        self._is_commodity = data.get("is_commodity")
        self._type = data.get("type")
        self._rarity_name = data.get("rarity_name")
        self._type_name = data.get("rarity_name")
        self._item_name = data.get("item_name")
        self._wear_name = data.get("wear_name")
        self._description = data.get("description")
        self._collection = data.get("collection")
        self._badges = data.get("badges")
        self._serialized_inspect = data.get("serialized_inspect")
        self._gs_sig = data.get("gs_sig")

    @property
    def asset_id(self) -> Optional[int]:
        return self._asset_id

    @property
    def def_index(self) -> Optional[int]:
        return self._def_index

    @property
    def paint_index(self) -> Optional[float]:
        return self._paint_index

    @property
    def paint_seed(self) -> Optional[float]:
        return self._paint_seed

    @property
    def float_value(self) -> Optional[float]:
        return self._float_value

    @property
    def icon_url(self) -> Optional[str]:
        return self._icon_url

    @property
    def d_param(self) -> Optional[int]:
        return self._d_param

    @property
    def is_stattrak(self) -> Optional[bool]:
        return self._is_stattrak

    @property
    def is_souvenir(self) -> Optional[bool]:
        return self._is_souvenir

    @property
    def rarity(self) -> Optional[str]:
        return self._rarity

    @property
    def quality(self) -> Optional[int]:
        return self._quality

    @property
    def market_hash_name(self) -> Optional[str]:
        return self._market_hash_name

    @property
    def low_rank(self) -> Optional[int]:
        return self._low_rank

    @property
    def stickers(self) -> Optional[List[Sticker]]:
        if self._stickers is not None:
            return [Sticker(data=sticker) for sticker in self._stickers]
        return None

    @property
    def tradable(self) -> Optional[bool]:
        return self._tradable

    @property
    def inspect_link(self) -> Optional[str]:
        return self._inspect_link

    @property
    def has_screenshot(self) -> Optional[bool]:
        return self._has_screenshot

    @property
    def cs2_screenshot_id(self) -> Optional[int]:
        return self._cs2_screenshot_id

    @property
    def cs2_screenshot_at(self) -> Optional[str]:
        return self._cs2_screenshot_at

    @property
    def is_commodity(self) -> Optional[bool]:
        return self._is_commodity

    @property
    def type(self) -> Optional[str]:
        return self._type

    @property
    def rarity_name(self) -> Optional[str]:
        return self._rarity_name

    @property
    def type_name(self) -> Optional[str]:
        return self._type_name

    @property
    def item_name(self) -> Optional[str]:
        return self._item_name

    @property
    def wear_name(self) -> Optional[str]:
        return self._wear_name

    @property
    def description(self) -> Optional[str]:
        return self._description

    @property
    def collection(self) -> Optional[str]:
        return self._collection

    @property
    def badges(self) -> Optional[list]:
        return self._badges

    @property
    def serialized_inspect(self) -> Optional[str]:
        return self._serialized_inspect

    @property
    def gs_sig(self) -> Optional[str]:
        return self._gs_sig
