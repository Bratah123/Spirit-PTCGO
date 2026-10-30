from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import poke_dex_handy

card = ItemCardDef(
    guid="f7a7239d-41b0-513e-9374-b71d9d71612e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeDexHANDY909.Name",
    display_name="PokéDex HANDY909",
    searchable_by=["PokéDex HANDY909", "PokéDex", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=poke_dex_handy,
)
