"""STUB: effect not implemented — do not guess mechanics.
Jynx (EX10 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import scorching_light_flip, stages_prevent_effects_no_weakness, freeze_light


card = PokemonCardDef(
    guid="20c16008-2147-56ea-b8a0-7d16f97eb649",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=124,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Jynx is an Evolved Pok\u00e9mon, prevent all effects of opponent's attacks, except damage, done to Jynx, and Jynx has no Weakness.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=stages_prevent_effects_no_weakness(),
        ),
        Attack(
            title="Freeze Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=scorching_light_flip(),
        ),
        Attack(
            title="Pure Power",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=freeze_light(),
        ),
    ],
)