"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_sunkern_114_sun_soak,
)

card = PokemonCardDef(guid='2a58fad5-f7e1-5c97-b98a-986bd1e67343', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name', display_name='Sunkern', searchable_by=['Sunkern', 'Basic', 'Sunkern'], subtypes=['Basic'], collector_number=114, set_code='DP3', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, family_id=191, abilities=[Attack(title='Sun Soak', game_text='Flip a coin. If heads, remove all damage counters from Sunkern, search your deck for an Evolution card that evolves from Sunkern, and put it onto Sunkern. (This counts as evolving Sunkern.) Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_sunkern_114_sun_soak()), Attack(title='Seed Bomb', cost={PokemonTypes.GRASS: 1}, damage=20)])
