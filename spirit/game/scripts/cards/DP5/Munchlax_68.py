"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="6db66ea1-2f81-5d81-aa2f-1662a6eca66e",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munchlax.Name",
    display_name="Munchlax",
    searchable_by=["Munchlax", "Basic", "Munchlax"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Snorlax from your hand onto Munchlax (this counts as evolving Munchlax) and remove all damage counters from Munchlax.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=baby_evolution_condition('Snorlax'),
            effect=baby_evolution('Snorlax'),
        ),
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)