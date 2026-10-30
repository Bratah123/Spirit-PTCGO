"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    fireworks_flip_discard,
)

card = PokemonCardDef(guid='1008b7d3-04b2-56f7-b59f-6a7d52de4e4f', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name', display_name='Quilava', searchable_by=['Quilava', 'Stage 1', 'Quilava'], subtypes=['Stage 1'], collector_number=60, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name', family_id=155, abilities=[Attack(title='Fireworks', game_text='Flip a coin. If tails, discard a Fire Energy attached to Quilava.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=fireworks_flip_discard(40))])
