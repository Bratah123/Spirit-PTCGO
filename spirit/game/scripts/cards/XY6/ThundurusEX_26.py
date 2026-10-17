"""STUB: effect not implemented — do not guess mechanics.
Thundurus-EX (XY6 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8290bf41-0414-50f2-8db8-a363f1388118",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "ThundurusEX"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=642,
    abilities=[
        Attack(
            title="Headlock",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Voltage Rush",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)