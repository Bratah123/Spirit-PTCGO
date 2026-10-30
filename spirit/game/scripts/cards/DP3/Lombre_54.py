"""STUB: effect not implemented — do not guess mechanics.
Lombre (DP3 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea769771-e044-531c-96e2-f7d73b80ecc4",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    display_name="Lombre",
    searchable_by=["Lombre", "Stage 1", "Lombre"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    family_id=270,
    abilities=[
        Attack(
            title="Torment",
            game_text="Flip a coin. If heads, your opponent can't play any Supporter cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Absorb",
            game_text="Remove 2 damage counters from Lombre.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)