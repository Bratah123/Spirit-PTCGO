"""STUB: effect not implemented — do not guess mechanics.
Smeargle (EX10 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import makeover_energy_swap
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="fb158a75-1828-5f42-9006-63be10a64d9c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Ability(
            title="Makeover",
            game_text="Once during your turn (before your attack), you may discard a basic Energy card attached to 1 of your Pok\u00e9mon (excluding Pok\u00e9mon-ex). If you do, search your discard pile for a basic Energy card (excluding the one you discarded) and attach it to that Pok\u00e9mon. This power can't be used if Smeargle is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            # STUB: ability effect not implemented
            effect=makeover_energy_swap(),
        ),
        Attack(
            title="Split Spiral Punch",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)