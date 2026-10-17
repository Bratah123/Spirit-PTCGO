"""STUB: effect not implemented — do not guess mechanics.
Malamar-EX (XY4 #58): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1f8682c8-7904-5dda-a588-e2c88e2f9be5",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarEX.Name",
    display_name="Malamar-EX",
    searchable_by=["Malamar-EX", "Basic", "EX", "MalamarEX"],
    subtypes=["Basic", "EX"],
    collector_number=58,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=687,
    abilities=[
        Ability(
            title="Hyper Hypnosis",
            game_text="When you attach an Energy from your hand to this Pok\u00e9mon, you may use this Ability. Your opponent's Active Pok\u00e9mon is now Asleep.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="MAXamar",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)