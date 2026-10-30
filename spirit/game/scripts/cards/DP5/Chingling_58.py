"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.dp import mud_spit_snipe


card = PokemonCardDef(
    guid="e14b3ee2-3c62-5cfc-b6ed-663d292fb30f",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chingling.Name",
    display_name="Chingling",
    searchable_by=["Chingling", "Basic", "Chingling"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=433,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Chimecho from your hand onto Chingling (this counts as evolving Chingling) and remove all damage counters from Chingling.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=baby_evolution('Chimecho'),
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Chimecho'),
        ),
        Attack(
            title="Uproar",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={},
            effect=mud_spit_snipe(10),
        ),
    ],
)