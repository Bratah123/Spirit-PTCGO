"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_darkrai_3_darkness_pursuit,
    dp4_darkrai_3_reach_over,
)

card = PokemonCardDef(guid='c45f196e-008b-5f86-97a1-f22b6a23e0f5', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name', display_name='Darkrai', searchable_by=['Darkrai', 'Basic', 'Darkrai'], subtypes=['Basic'], collector_number=3, set_code='DP4', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=491, abilities=[Attack(title='Reach Over', game_text='Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={}, effect=dp4_darkrai_3_reach_over()), Attack(title='Darkness Pursuit', game_text="If the Defending Pokémon is Cresselia, this attack's base damage is 100.", cost={PokemonTypes.DARKNESS: 3}, damage=50, effect=dp4_darkrai_3_darkness_pursuit())])
