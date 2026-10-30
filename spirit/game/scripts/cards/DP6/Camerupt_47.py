"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_camerupt_47_eruption,
    dp6_camerupt_47_take_down,
)

card = PokemonCardDef(guid='baea33c3-9e5b-51ee-a40c-876b341e340e', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name', display_name='Camerupt', searchable_by=['Camerupt', 'Stage 1', 'Camerupt'], subtypes=['Stage 1'], collector_number=47, set_code='DP6', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name', family_id=322, abilities=[Attack(title='Eruption', game_text='Each player discards the top of his or her deck. This attack does 30 damage plus 30 more damage for each Energy card discarded in this way.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=dp6_camerupt_47_eruption()), Attack(title='Take Down', game_text='Camerupt does 20 damage to itself.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=80, effect=dp6_camerupt_47_take_down())])
