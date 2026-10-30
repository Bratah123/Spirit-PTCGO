"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_diglett_85_down_draw,
)

card = PokemonCardDef(guid='f866b5b4-eea2-55a8-8bb2-f5af742d9394', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name', display_name='Diglett', searchable_by=['Diglett', 'Basic', 'Diglett'], subtypes=['Basic'], collector_number=85, set_code='DP3', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=50, abilities=[Attack(title='Down Draw', game_text='Draw a card from the bottom of your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_diglett_85_down_draw()), Attack(title='Mud Spatter', cost={PokemonTypes.FIGHTING: 2}, damage=30)])
