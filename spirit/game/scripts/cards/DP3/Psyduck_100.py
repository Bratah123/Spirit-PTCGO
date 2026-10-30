"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_psyduck_100_delusion,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='db3722a9-e0df-5f21-911f-0b1cb5899d7c', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name', display_name='Psyduck', searchable_by=['Psyduck', 'Basic', 'Psyduck'], subtypes=['Basic'], collector_number=100, set_code='DP3', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=54, abilities=[Attack(title='Delusion', game_text='If Psyduck is Confused, draw 2 cards.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_psyduck_100_delusion()), Attack(title='Migraine', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused. If tails, Psyduck is now Confused.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
