from typing import Dict, Any, Optional
from warnings import deprecated


class StickerReference:
    __slots__ = (
        "_price",
        "_quantity",
        "_updated_at"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._price = data.get("price", "")
        self._quantity = data.get("quantity")
        self._updated_at = data.get("updated_at")

    @property
    def price(self) -> Optional[float]:
        return self._price

    @property
    def quantity(self) -> Optional[int]:
        return self._quantity

    @property
    def updated_at(self) -> Optional[str]:
        return self._updated_at


class Sticker:
    __slots__ = (
        "_sticker_id",
        "_slot",
        "_wear",
        "_offset_x",
        "_offset_y",
        "_icon_url",
        "_name",
        "_reference"
    )

    def __init__(self, *, data: Dict[str, Any]):
        self._sticker_id = data.get("stickerId")
        self._slot = data.get("slot")
        self._wear = data.get("wear")
        self._offset_x = data.get("offset_x")
        self._offset_y = data.get("offset_y")
        self._icon_url = data.get("icon_url")
        self._name = data.get("name")
        self._reference = data.get("reference")

    @property
    @deprecated("'stickerId' is deprecated; use 'sticker_id' instead.")
    def stickerId(self) -> Optional[int]:
        return self.sticker_id

    @property
    def sticker_id(self) -> Optional[int]:
        return self._sticker_id

    @property
    def slot(self) -> Optional[int]:
        return self._slot

    @property
    def wear(self) -> Optional[float]:
        return self._wear

    @property
    def icon_url(self) -> Optional[str]:
        return self._icon_url

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def reference(self) -> Optional[StickerReference]:
        if self._reference is not None:
            return StickerReference(data=self._reference)
        return None
