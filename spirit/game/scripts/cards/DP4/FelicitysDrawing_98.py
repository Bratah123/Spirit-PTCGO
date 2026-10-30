"""Felicity's Drawing (DP4 #98)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import felicitys_drawing

card = SupporterCardDef(
    guid="c8485c61-52d1-52ce-b276-6540a31c13a7",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FelicitysDrawing.Name",
    display_name="Felicity's Drawing",
    searchable_by=["Felicity's Drawing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    effect=felicitys_drawing(),
)
