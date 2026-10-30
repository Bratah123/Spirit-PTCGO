"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    dp6_buneary_86_rest,
)

card = PokemonCardDef(guid='2ee4343e-62ae-5b77-95b8-05cc66390f82', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name', display_name='Buneary', searchable_by=['Buneary', 'Basic', 'Buneary'], subtypes=['Basic'], collector_number=86, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=427, abilities=[Attack(title='Rest', game_text='Remove all Special Conditions and 4 damage counters from Buneary. Buneary is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=dp6_buneary_86_rest()), Attack(title='Double Kick', game_text='Flip 2 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(2, per_heads=20))])
