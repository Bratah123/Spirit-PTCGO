"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp4_zigzagoon_96_pull_out,
)

card = PokemonCardDef(guid='651ec7d6-7054-50b8-9fd6-9b411d3938ba', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name', display_name='Zigzagoon', searchable_by=['Zigzagoon', 'Basic', 'Zigzagoon'], subtypes=['Basic'], collector_number=96, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=263, abilities=[Attack(title='Pull Out', game_text='Search your discard pile for any 1 card, show it to your opponent, and put it on top of your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=dp4_zigzagoon_96_pull_out()), Attack(title='Double Stab', game_text='Flip 2 coins. This attack does 10 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=flip_damage(coins=2, per_heads=10))])
