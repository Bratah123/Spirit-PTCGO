"""STUB: effect not implemented — do not guess mechanics.
Lugia-EX (XY7 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="396fed67-66bf-5c52-b0ef-074ad11fe90a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "LugiaEX"],
    subtypes=["Basic", "EX"],
    collector_number=68,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title="Aero Ball",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Deep Hurricane",
            game_text="If there is any Stadium card in play, this attack does 70 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)