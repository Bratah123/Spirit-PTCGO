from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece
from spirit.game.attributes import Rarities

card = VUnionPieceCardDef(
    guid="fd2c702c-1e81-575d-98a9-762626c36c90",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name",
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    collector_number=159,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MewtwoVUNION_Combined",
    piece=VUnionPiece.TOP_LEFT,
)
