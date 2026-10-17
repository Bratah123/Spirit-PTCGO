"""STUB: effect not implemented — do not guess mechanics.
M Aggron-EX (XY5 #154): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e47e11fb-50bd-58f9-a4d2-d8ceafe635fe",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAggronEX.Name",
    display_name="M Aggron-EX",
    searchable_by=["M Aggron-EX", "MEGA", "EX", "MAggronEX"],
    subtypes=["MEGA", "EX"],
    collector_number=154,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AggronEX.Name",
    family_id=306,
    abilities=[
        Attack(
            title="Megaton Slam",
            game_text="You may flip a coin. If heads, this attack does 120 more damage. If tails, this attack does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)