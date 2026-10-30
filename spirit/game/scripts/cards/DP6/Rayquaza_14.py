"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_rayquaza_14_sky_judgement,
    dp6_rayquaza_14_speed_gain,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='a4f643a1-2861-5245-9568-0da363d05191', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name', display_name='Rayquaza', searchable_by=['Rayquaza', 'Basic', 'Rayquaza'], subtypes=['Basic'], collector_number=14, set_code='DP6', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=384, abilities=[Ability(title='Speed Gain', game_text="Once during your turn (before your attack), you may flip a coin until you get tails. For each heads, search your discard pile for a basic Fire Energy card or a basic Lightning Energy card and attach it to Rayquaza. This power can't be used if Rayquaza is affected by a Special Condition or if you have another Rayquaza in play.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_rayquaza_14_speed_gain(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Sky Judgement', game_text='Discard all Energy attached to Rayquaza.', cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2}, damage=150, effect=dp6_rayquaza_14_sky_judgement())])
