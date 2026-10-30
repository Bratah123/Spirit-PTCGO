"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Houndour (EX4 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="a81bd569-4333-5167-b89c-259bd878f7d9",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundour.Name",
    display_name="Team Magma's Houndour",
    searchable_by=["Team Magma's Houndour", "Basic", "TeamMagmasHoundour"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Super Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)