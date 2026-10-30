"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='edcc8e38-b892-5c0f-85e1-b16dd0e9cd79', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name', display_name='Gligar', searchable_by=['Gligar', 'Basic', 'Gligar'], subtypes=['Basic'], collector_number=94, set_code='DP6', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=207, abilities=[Attack(title='Light Poison', game_text='Flip a coin. If tails, this attack does nothing. If heads, the Defending Pokémon is now Poisoned.', cost={}, damage=10, effect=flip_or_nothing()), Attack(title='Jump On', game_text='Flip a coin. If heads, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.FIGHTING: 1}, damage=10, damage_operator='+', effect=flip_bonus(10))])
