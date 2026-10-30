"""STUB: effect not implemented — do not guess mechanics.
Shiftry (DP1 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import darkness_fan, poke_power_condition, is_active_pokemon
from spirit.game.data_utils import Activations


card = PokemonCardDef(
    guid="be4e0228-9786-590c-b00f-a4af25c8e82c",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Darkness Fan",
            game_text="Once during your turn (before your attack), if Shiftry is your Active Pok\u00e9mon, you may flip a coin. If heads, choose 1 Evolved Pok\u00e9mon on your opponent's Bench, remove the highest Stage Evolution card from that Pok\u00e9mon, and put it back into his or her hand. This power can't be used if Shiftry is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(is_active_pokemon),
            activation=Activations.ONCE_PER_TURN,
            effect=darkness_fan(),
        ),
        Attack(
            title="Spirit Dance",
            game_text="Flip 2 coins. This attack does 50 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)