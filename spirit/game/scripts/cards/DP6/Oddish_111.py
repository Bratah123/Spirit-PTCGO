"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp6_oddish_111_blot,
)

card = PokemonCardDef(guid='70a41834-aab1-5c27-a877-f564c6b728c8', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name', display_name='Oddish', searchable_by=['Oddish', 'Basic', 'Oddish'], subtypes=['Basic'], collector_number=111, set_code='DP6', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=43, abilities=[Attack(title='Stun Spore', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Blot', game_text='Remove 1 damage counter from Oddish.', cost={PokemonTypes.GRASS: 1}, damage=10, effect=dp6_oddish_111_blot())])
