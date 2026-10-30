from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import poke_nav
from spirit.game.card_effects.trainers import deck_nonempty


card = ItemCardDef(
    guid="ca85ee98-a445-53c9-9a7e-57cc8972f51c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=poke_nav,
)
