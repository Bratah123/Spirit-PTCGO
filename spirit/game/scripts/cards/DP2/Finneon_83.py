"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    elegant_swim_protect,
)

card = PokemonCardDef(guid='9cc01165-af87-5e1e-b99d-7c3b33a287d2', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name', display_name='Finneon', searchable_by=['Finneon', 'Basic', 'Finneon'], subtypes=['Basic'], collector_number=83, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=456, abilities=[Attack(title='Elegant Swim', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Finneon during your opponent's next turn.", cost={PokemonTypes.WATER: 1}, effect=elegant_swim_protect()), Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
