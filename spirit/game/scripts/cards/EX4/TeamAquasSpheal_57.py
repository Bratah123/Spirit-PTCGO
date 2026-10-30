"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Spheal (EX4 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import delayed_condition

card = PokemonCardDef(
    guid="ae4f6ce5-6497-526d-975a-6db9ca814241",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    display_name="Team Aqua's Spheal",
    searchable_by=["Team Aqua's Spheal", "Basic", "TeamAquasSpheal"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Aqua Trance",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=delayed_condition(SpecialConditions.ASLEEP),
        ),
    ],
)