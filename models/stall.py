from typing import List, Dict, Any
from .listing import Listing


class Stall:
    def __init__(self, *, data: Dict[str, Any]) -> None:
        listings_data = data.get('data')
        if listings_data is None:
            self._listings = []
        else:
            self._listings = [Listing(data=item) for item in listings_data]

    @property
    def listings(self) -> List[Listing]:
        return self._listings
