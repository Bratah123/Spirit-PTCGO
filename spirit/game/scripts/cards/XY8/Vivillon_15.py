"""STUB: effect not implemented — do not guess mechanics.
Vivillon (XY8 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="af80e064-f379-5ef7-99ef-3ed4383dd858",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Energy Color",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sleep Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)