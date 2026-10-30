"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    flail_damage_counters,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='9267dbdd-f6a6-5fa3-bd04-d38a704c82e6', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name', display_name='Sudowoodo', searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'], subtypes=['Basic'], collector_number=48, set_code='DP5', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=185, abilities=[Attack(title='Flail', game_text='Does 10 damage times the number of damage counters on Sudowoodo.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flail_damage_counters(per=10)), Attack(title='Wood Hammer', game_text='Sudowoodo does 30 damage to itself.', cost={PokemonTypes.FIGHTING: 2}, damage=50, effect=recoil_attack(30, damage=50))])
