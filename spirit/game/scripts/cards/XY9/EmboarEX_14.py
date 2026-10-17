"""STUB: effect not implemented — do not guess mechanics.
Emboar-EX (XY9 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3adff194-a0a5-5445-a67b-67a031d05544",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmboarEX.Name",
    display_name="Emboar-EX",
    searchable_by=["Emboar-EX", "Basic", "EX", "EmboarEX"],
    subtypes=["Basic", "EX"],
    collector_number=14,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=500,
    abilities=[
        Attack(
            title="Spiral Punch",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Strong Flare",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)