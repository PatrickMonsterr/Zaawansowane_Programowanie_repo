"""Pobiera 20 pierwszych browarów z Open Brewery DB i wyświetla je jako obiekty Brewery.

Dokumentacja API: https://www.openbrewerydb.org/documentation
Wymagana biblioteka: requests  (pip install requests)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries"
LIMIT = 20


def _to_float(value: Any) -> Optional[float]:
    """API zwraca współrzędne jako string lub null - zamieniamy na float/None."""
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: Optional[str] = None   # pole przestarzałe (deprecated), zastąpione state_province
    street: Optional[str] = None  # pole przestarzałe (deprecated), zastąpione address_1

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Brewery:
        """Tworzy obiekt z słownika zwróconego przez API."""
        return cls(
            id=data["id"],
            name=data["name"],
            brewery_type=data.get("brewery_type", ""),
            address_1=data.get("address_1"),
            address_2=data.get("address_2"),
            address_3=data.get("address_3"),
            city=data.get("city"),
            state_province=data.get("state_province"),
            postal_code=data.get("postal_code"),
            country=data.get("country"),
            longitude=_to_float(data.get("longitude")),
            latitude=_to_float(data.get("latitude")),
            phone=data.get("phone"),
            website_url=data.get("website_url"),
            state=data.get("state"),
            street=data.get("street"),
        )

    def __str__(self) -> str:
        address = ", ".join(
            part
            for part in (
                self.address_1,
                self.address_2,
                self.address_3,
                self.postal_code,
                self.city,
                self.state_province,
                self.country,
            )
            if part
        )
        coords = (
            f"{self.latitude}, {self.longitude}"
            if self.latitude is not None and self.longitude is not None
            else "brak danych"
        )
        return (
            f"Browar: {self.name} (id: {self.id})\n"
            f"  Typ:          {self.brewery_type}\n"
            f"  Adres:        {address or 'brak danych'}\n"
            f"  Współrzędne:  {coords}\n"
            f"  Telefon:      {self.phone or 'brak danych'}\n"
            f"  Strona www:   {self.website_url or 'brak danych'}"
        )


def fetch_breweries(limit: int = LIMIT) -> list[dict[str, Any]]:
    """Pobiera `limit` pierwszych browarów z API."""
    response = requests.get(API_URL, params={"per_page": limit}, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    try:
        raw_data = fetch_breweries(LIMIT)
    except requests.RequestException as exc:
        print(f"Błąd podczas łączenia z API: {exc}")
        return

    breweries: list[Brewery] = [Brewery.from_dict(item) for item in raw_data]

    for number, brewery in enumerate(breweries, start=1):
        print(f"--- {number}/{len(breweries)} ---")
        print(brewery)
        print()


if __name__ == "__main__":
    main()