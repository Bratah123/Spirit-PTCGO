"""STUB: effect not implemented — do not guess mechanics.
Cloyster (DP3 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a98f9f57-994c-5892-9ca5-39eaa5651fba",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=90,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, prevent all damage done to Cloyster by attacks during your opponent's next turn.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Spine Missile",
            game_text="Flip 4 coins. For each heads, choose an opponent's Pok\u00e9mon in play and this attack does 20 damage to those Pok\u00e9mon. (You may choose the same Pok\u00e9mon more than once.) (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)