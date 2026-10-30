"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import (
    dp5_aipom_50_hand_trick,
)

card = PokemonCardDef(guid='2a905f28-7c53-570f-93e7-5558b82ca938', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name', display_name='Aipom', searchable_by=['Aipom', 'Basic', 'Aipom'], subtypes=['Basic'], collector_number=50, set_code='DP5', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=190, abilities=[Attack(title='Collect', game_text='Draw a card.', cost={PokemonTypes.COLORLESS: 1}, effect=draw_attack(1)), Attack(title='Hand Trick', game_text="Return Aipom and all cards attached to it to your hand. (If you don't have any Benched Pokémon, this attack does nothing.)", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp5_aipom_50_hand_trick())])
