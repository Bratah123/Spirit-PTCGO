"""STUB: effect not implemented — do not guess mechanics.
Hoopa-EX (XY7 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2106f4c0-6354-5c3a-b801-31d893995379",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name",
    display_name="Hoopa-EX",
    searchable_by=["Hoopa-EX", "Basic", "EX", "HoopaEX"],
    subtypes=["Basic", "EX"],
    collector_number=36,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Ability(
            title="Scoundrel Ring",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may search your deck for up to 3 Pok\u00e9mon-EX (except for Hoopa-EX), reveal them, and put them into your hand. Shuffle your deck afterward.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hyperspace Fury",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)