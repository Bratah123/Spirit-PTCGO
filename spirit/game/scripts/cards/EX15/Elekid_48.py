"""STUB: effect not implemented — do not guess mechanics.
Elekid δ (EX15 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="5dee685c-1436-5982-8a92-f55515203d20",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid δ",
    searchable_by=["Elekid \u03b4", "Basic", "Elekid"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Electabuzz from your hand onto Elekid (this counts as evolving Elekid) and remove all damage counters from Elekid.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Electabuzz'),
            effect=baby_evolution('Electabuzz'),
        ),
        Attack(
            title="Thunder Spear",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, pool='any'),
        ),
    ],
)