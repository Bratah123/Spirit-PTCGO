"""STUB: effect not implemented — do not guess mechanics.
Pidgeot-EX (XY12 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8bf751da-9d82-5285-ac92-6a2569b7cf3b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotEX.Name",
    display_name="Pidgeot-EX",
    searchable_by=["Pidgeot-EX", "Basic", "EX", "PidgeotEX"],
    subtypes=["Basic", "EX"],
    collector_number=104,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=18,
    abilities=[
        Attack(
            title="Mirror Move",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does the same amount of damage to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Feather Lance",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)