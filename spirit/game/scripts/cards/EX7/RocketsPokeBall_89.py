from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import rockets_poke_ball

card = ItemCardDef(
    guid="1b53536b-8886-56bb-96f2-aa838456c2d5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsPokeBall.Name",
    display_name="Rocket's Poké Ball",
    searchable_by=["Rocket's Poké Ball", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=rockets_poke_ball,
)
