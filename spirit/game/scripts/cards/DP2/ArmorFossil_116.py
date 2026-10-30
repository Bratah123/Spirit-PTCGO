"""Armor Fossil (DP2 #116)."""
from spirit.game.data_utils import FossilItemCardDef, Ability
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability
from spirit.game.card_effects.dp import armor_stone_passive

card = FossilItemCardDef(
    guid="387c8fab-9c97-57f4-b557-3690609b8461",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossil.Name",
    display_name="Armor Fossil",
    searchable_by=["Armor Fossil", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[
        fossil_discard_ability(),
        Ability(
            title="Armor Stone",
            game_text="",
            ability_type=AbilityTypes.POKE_BODY,
            passive=armor_stone_passive(),
        ),
    ],
)
