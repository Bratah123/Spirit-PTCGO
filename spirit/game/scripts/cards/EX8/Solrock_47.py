"""STUB: effect not implemented — do not guess mechanics.
Solrock (EX8 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import reflected_beam_lunatone, scorching_light_flip, sunbeam_lunatone_hp


card = PokemonCardDef(
    guid="dd6904f8-05e9-51d5-82a2-445c95b1d8e9",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Sunbeam",
            game_text="The maximum HP for each Lunatone you have in play is now 80.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=sunbeam_lunatone_hp(),
        ),
        Attack(
            title="Scorching Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=scorching_light_flip(),
        ),
        Attack(
            title="Reflected Beam",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon for each Lunatone you have in play. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=reflected_beam_lunatone(),
        ),
    ],
)