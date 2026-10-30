"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    scrunch_protect,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='43f5c34c-cccf-5091-aa21-cebc00e89831', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name', display_name='Chansey', searchable_by=['Chansey', 'Basic', 'Chansey'], subtypes=['Basic'], collector_number=76, set_code='DP2', rarity=Rarities.Common, hp=100, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=113, abilities=[Attack(title='Scrunch', game_text="Flip a coin. If heads, prevent all damage done to Chansey by attacks during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, effect=scrunch_protect()), Attack(title='Double-edge', game_text='Chansey does 60 damage to itself.', cost={PokemonTypes.COLORLESS: 4}, damage=80, effect=recoil_attack(60, damage=80))])
