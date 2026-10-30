from spirit.game.card_effects.ex import water_plant
"""STUB: effect not implemented — do not guess mechanics.
Horsea (EX7 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import swift_attack


card = PokemonCardDef(
    guid="fe4b41c5-1ac3-571d-97ea-c9cbc1582e63",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Water Plant",
            game_text="Search your discard pile for up to 2 Water Energy cards, show them to your opponent, and put them into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=water_plant(),
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
    ],
)