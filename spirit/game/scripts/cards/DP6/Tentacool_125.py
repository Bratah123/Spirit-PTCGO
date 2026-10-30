"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_vibrava_74_hyper_beam
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(guid='1217b174-e5bf-54c0-9eed-9f41a29dc6dc', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name', display_name='Tentacool', searchable_by=['Tentacool', 'Basic', 'Tentacool'], subtypes=['Basic'], collector_number=125, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=72, abilities=[Attack(title='Crystal Barrier', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Tentacool during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=flip_protection(prevent=True, effects_too=True, title='Crystal Barrier')), Attack(title='Mysterious Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.WATER: 1}, effect=dp3_vibrava_74_hyper_beam())])
