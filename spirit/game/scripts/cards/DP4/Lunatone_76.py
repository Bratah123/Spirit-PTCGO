"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_lunatone_76_gravity_change,
    dp4_lunatone_76_knock_over,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='b765a87a-052e-5c06-89f5-f1e0cea9a630', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name', display_name='Lunatone', searchable_by=['Lunatone', 'Basic', 'Lunatone'], subtypes=['Basic'], collector_number=76, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=337, abilities=[Ability(title='Gravity Change', game_text="Once during your turn (before your attack), you may discard a card from your hand. Then, if you have Solrock in play, draw a card. This power can't be used if Lunatone is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_lunatone_76_gravity_change(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Knock Over', game_text='You may discard any Stadium card in play.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp4_lunatone_76_knock_over())])
