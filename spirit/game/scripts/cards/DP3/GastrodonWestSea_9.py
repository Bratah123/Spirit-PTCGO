"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_gastrodonwestsea_9_wild_waves,
    scaled_self_counters,
)

card = PokemonCardDef(guid='fdfe7060-eebf-535b-85d3-093384bebe4f', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.GastrodonWestSea.Name', display_name='Gastrodon West Sea', searchable_by=['Gastrodon West Sea', 'Stage 1', 'GastrodonWestSea'], subtypes=['Stage 1'], collector_number=9, set_code='DP3', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.ShellosWestSea.Name', family_id=422, abilities=[Attack(title='Raging Flood', game_text='Does 20 damage plus 10 more damage for each damage counter on Gastrodon West Sea. Then, remove 2 damage counters from Gastrodon West Sea.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=scaled_self_counters(20, 10)), Attack(title='Wild Waves', game_text="Put 1 damage counter on each Benched Pokémon (both yours and your opponent's).", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3}, damage=80, effect=dp3_gastrodonwestsea_9_wild_waves())])
