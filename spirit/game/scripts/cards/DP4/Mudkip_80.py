"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_mudkip_80_endeavor,
)

card = PokemonCardDef(guid='c0d09c83-7255-558a-81ba-bf9258a0780d', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name', display_name='Mudkip', searchable_by=['Mudkip', 'Basic', 'Mudkip'], subtypes=['Basic'], collector_number=80, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=258, abilities=[Attack(title='Mud Spatter', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Endeavor', game_text='Flip 2 coins. This attack does 30 damage plus 20 more damage for each heads.', cost={PokemonTypes.COLORLESS: 3}, damage=30, damage_operator='+', effect=dp4_mudkip_80_endeavor())])
