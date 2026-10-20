"""STUB: effect not implemented — do not guess mechanics.
Chesnaught BREAK (XY8 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e8f54453-bf41-5edd-84a8-6cea6f241f3f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChesnaughtBREAK.Name",
    display_name="Chesnaught BREAK",
    searchable_by=["Chesnaught BREAK", "BREAK", "ChesnaughtBREAK"],
    subtypes=["BREAK"],
    collector_number=12,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Tough Hammer",
            game_text="This Pok\u00e9mon does 30 damage to itself. This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)