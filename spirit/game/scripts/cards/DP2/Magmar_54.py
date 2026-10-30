"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    flamethrower_discard,
)

card = PokemonCardDef(guid='f01306a2-1e35-58c7-8cbe-2a7439d64ca3', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name', display_name='Magmar', searchable_by=['Magmar', 'Basic', 'Magmar'], subtypes=['Basic'], collector_number=54, set_code='DP2', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=126, abilities=[Attack(title='Flare', cost={PokemonTypes.FIRE: 1}, damage=20), Attack(title='Flamethrower', game_text='Discard an Energy attached to Magmar.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=flamethrower_discard(50))])
