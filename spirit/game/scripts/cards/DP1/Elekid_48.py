"""STUB: effect not implemented — do not guess mechanics.
Elekid (DP1 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.dp import outlet_search


card = PokemonCardDef(
    guid="e7c067a3-e1c4-52af-8344-e039279139c2",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Basic", "Elekid"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=239,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Electabuzz from your hand onto Elekid (this counts as evolving Elekid) and remove all damage counters from Elekid.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Electabuzz'),
            effect=baby_evolution('Electabuzz'),
        ),
        Attack(
            title="Outlet",
            game_text="Search your deck for a Lightning Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=outlet_search(),
        ),
    ],
)