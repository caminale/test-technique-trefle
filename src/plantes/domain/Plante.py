from dataclasses import dataclass
from typing import List

@dataclass
class Plante:
    id: int
    common_name: str
    slug: str
    scientific_name: str
    year: str
    bibliography: str
    author: str
    status: str
    rank: str
    family_common_name: str
    genus_id: int
    image_url: str
    synonyms: List[str]
    genus: str
    family: str
    links: List[str]