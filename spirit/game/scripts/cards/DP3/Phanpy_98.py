"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    flail_damage_counters,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='ca17e4bb-5cf1-534a-8b5a-6000ab7d163c', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name', display_name='Phanpy', searchable_by=['Phanpy', 'Basic', 'Phanpy'], subtypes=['Basic'], collector_number=98, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=231, abilities=[Attack(title='Flail', game_text='Does 10 damage times the number of damage counters on Phanpy.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flail_damage_counters(per=10)), Attack(title='Take Down', game_text='Phanpy does 10 damage to itself.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=recoil_attack(10, damage=30))])
