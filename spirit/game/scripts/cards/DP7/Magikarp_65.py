"""STUB: effect not implemented — do not guess mechanics.
Magikarp (DP7 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_magikarp_65_sea_spray,
)

card = PokemonCardDef(guid='b1af9267-d138-5c7a-b765-3514ea05c750', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name', display_name='Magikarp', searchable_by=['Magikarp', 'Basic', 'Magikarp'], subtypes=['Basic'], collector_number=65, set_code='DP7', rarity=Rarities.Common, hp=30, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=129, abilities=[Attack(title='Sea Spray', game_text='Flip a coin until you get tails. For each heads, draw a card.', cost={}, effect=dp7_magikarp_65_sea_spray()), Attack(title='Splash', cost={PokemonTypes.WATER: 1}, damage=10)])
