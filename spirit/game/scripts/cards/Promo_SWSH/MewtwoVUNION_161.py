from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece
from spirit.game.attributes import Rarities

card = VUnionPieceCardDef(
    guid="36ed17ee-eed6-5d34-8d88-936af7fdcfd0",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name",
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    collector_number=161,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MewtwoVUNION_Combined",
    piece=VUnionPiece.BOTTOM_LEFT,
)
