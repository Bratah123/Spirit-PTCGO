"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Rhydon (EX4 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import ignore_resistance_attack, conditions_if
from spirit.game.card_effects.ex import defender_has_team


card = PokemonCardDef(
    guid="e1ca7414-6d71-5f4d-9413-a4935bf70fa6",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhydon.Name",
    display_name="Team Magma's Rhydon",
    searchable_by=["Team Magma's Rhydon", "Stage 1", "TeamMagmasRhydon"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Magma Jab",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
        Attack(
            title="Shoot Down",
            game_text="If the Defending Pok\u00e9mon has Team Aqua in its name, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_has_team("Team Aqua"), SpecialConditions.CONFUSED),
        ),
    ],
)