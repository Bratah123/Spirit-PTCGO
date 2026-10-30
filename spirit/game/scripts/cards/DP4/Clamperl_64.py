"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='c4044504-8d2a-54a6-9547-b66bdc764a65', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', display_name='Clamperl', searchable_by=['Clamperl', 'Basic', 'Clamperl'], subtypes=['Basic'], collector_number=64, set_code='DP4', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=366, abilities=[Attack(title='Clamp', game_text='Flip a coin. If tails, this attack does nothing. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=flip_or_nothing()), Attack(title='Sparkling Pearl', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20)])
