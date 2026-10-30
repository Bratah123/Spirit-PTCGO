"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_cresselia_2_lunar_dance,
    dp4_cresselia_2_moon_twinkle,
)

card = PokemonCardDef(guid='17dfa830-b31c-5ac8-b6b4-251f23d1d721', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name', display_name='Cresselia', searchable_by=['Cresselia', 'Basic', 'Cresselia'], subtypes=['Basic'], collector_number=2, set_code='DP4', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=488, abilities=[Attack(title='Moon Twinkle', game_text='If there is any Stadium card in play, remove 2 damage counters from Cresselia.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=dp4_cresselia_2_moon_twinkle()), Attack(title='Lunar Dance', game_text='You may discard 2 Energy attached to Cresselia. If you do, remove all damage counters from 1 of your Benched Pokémon.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp4_cresselia_2_lunar_dance())])
