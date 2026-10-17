"""STUB: effect not implemented — do not guess mechanics.
Machamp-EX (XY7 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cfa54d2-25da-5c83-bee0-bf9776eb29ea",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampEX.Name",
    display_name="Machamp-EX",
    searchable_by=["Machamp-EX", "Basic", "EX", "MachampEX"],
    subtypes=["Basic", "EX"],
    collector_number=90,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Steaming Mad",
            game_text="This attack does 20 damage times the number of damage counters on this Pok\u00e9mon. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crazy Hammer",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)