"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Carvanha (TATM #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b61e8ff2-bb43-51b1-967b-2e0f793647d1",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    display_name="Team Aqua's Carvanha",
    searchable_by=["Team Aqua's Carvanha", "Basic", "TeamAquasCarvanha"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Attack(
            title="Fin Smack",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)