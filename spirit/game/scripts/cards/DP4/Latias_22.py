"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_latias_22_mist_ball,
    heal_attack,
)

card = PokemonCardDef(guid='bb0a49c9-0944-52dc-a8d3-506beec79a1a', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name', display_name='Latias', searchable_by=['Latias', 'Basic', 'Latias'], subtypes=['Basic'], collector_number=22, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=380, abilities=[Attack(title='Miraculous Light', game_text='Remove 2 damage counters and all Special Conditions from Latias.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=heal_attack(20)), Attack(title='Mist Ball', game_text='Discard a Fire Energy and a Water Energy attached to Latias.', cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=80, effect=dp4_latias_22_mist_ball())])
