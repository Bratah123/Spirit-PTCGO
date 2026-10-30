"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_registeel_39_regi_heal,
    dp6_registeel_39_rotating_claws,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='f3291f66-4398-5e52-910e-b122da959e12', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name', display_name='Registeel', searchable_by=['Registeel', 'Basic', 'Registeel'], subtypes=['Basic'], collector_number=39, set_code='DP6', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=379, abilities=[Ability(title='Regi Heal', game_text="Once during your turn (before your attack), you may discard 2 cards from your hand. Then, remove 3 damage counters from Registeel. This power can't be used if Registeel is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_registeel_39_regi_heal(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Rotating Claws', game_text='You may discard an Energy card attached to Registeel. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Registeel.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=dp6_registeel_39_rotating_claws())])
