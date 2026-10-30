"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Carvanha (EX4 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ee32b755-98cc-5c73-adac-cdcdf94610f2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    display_name="Team Aqua's Carvanha",
    searchable_by=["Team Aqua's Carvanha", "Basic", "TeamAquasCarvanha"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Poison Fang",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)