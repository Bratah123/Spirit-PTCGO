from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import rotom_dex_poke_finder

card = ItemCardDef(
    guid="21dff0ef-6275-5b93-b3eb-171cd14943b8",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDexPokeFinderMode.Name",
    display_name="Rotom Dex Poké Finder Mode",
    searchable_by=["Rotom Dex Pok\u00e9 Finder Mode", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=rotom_dex_poke_finder,)
