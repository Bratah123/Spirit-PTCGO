"""STUB: effect not implemented — do not guess mechanics.
Keldeo (Promo_XY #XY118): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="062eb010-9c15-5134-a959-2ddf7b46919a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name",
    display_name="Keldeo",
    searchable_by=["Keldeo", "Basic", "Keldeo"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Justified",
            game_text="This Pok\u00e9mon's attacks do 50 more damage to your opponent's Darkness Pok\u00e9mon (before applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pok\u00e9mon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)