"""STUB: effect not implemented — do not guess mechanics.
Azurill (DP1 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition


card = PokemonCardDef(
    guid="c479e7dd-8b80-5e69-ad9b-06bc5a213aef",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Marill from your hand onto Azurill (this counts a evolving Azurill) and remove all damage counters from Azurill.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=baby_evolution_condition('Marill'),
            effect=baby_evolution('Marill'),
        ),
        Attack(
            title="Delivery",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={},
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to='hand', prompt='Choose a card from your discard pile.'),
        ),
    ],
)