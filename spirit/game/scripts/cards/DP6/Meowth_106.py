"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp6_meowth_106_pay_day,
)

card = PokemonCardDef(guid='ab9495db-5489-5135-b095-e8764f438df5', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name', display_name='Meowth', searchable_by=['Meowth', 'Basic', 'Meowth'], subtypes=['Basic'], collector_number=106, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=52, abilities=[Attack(title='Pay Day', game_text='Flip a coin. If heads, draw a card.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=dp6_meowth_106_pay_day()), Attack(title='Fury Swipes', game_text='Flip 3 coins. This attack does 10 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='x', effect=flip_damage(3, per_heads=10))])
