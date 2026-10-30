"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.dp import (
    flail_damage_counters,
)

card = PokemonCardDef(guid='15e6a0ea-f1bb-5ee2-bba5-79af6daac06e', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name', display_name='Magikarp', searchable_by=['Magikarp', 'Basic', 'Magikarp'], subtypes=['Basic'], collector_number=89, set_code='DP2', rarity=Rarities.Common, hp=30, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=129, abilities=[Attack(title='Flail', game_text='Does 10 damage times the number of damage counters on Magikarp.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flail_damage_counters(10)), Attack(title='Dragon Rage', game_text='Flip 2 coins. If either of them is tails, this attack does nothing.', cost={PokemonTypes.WATER: 2}, damage=60, effect=flip_or_nothing(coins=2))])
