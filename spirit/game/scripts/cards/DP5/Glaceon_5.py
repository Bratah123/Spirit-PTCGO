"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_glaceon_5_snow_cloak,
    dp5_glaceon_5_speed_slide,
)

card = PokemonCardDef(guid='1ecebf40-4d90-505d-8810-d888eb1e63d2', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name', display_name='Glaceon', searchable_by=['Glaceon', 'Stage 1', 'Glaceon'], subtypes=['Stage 1'], collector_number=5, set_code='DP5', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Attack(title='Snow Cloak', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Glaceon during your opponent's next turn.", cost={PokemonTypes.WATER: 1}, damage=30, effect=dp5_glaceon_5_snow_cloak()), Attack(title='Speed Slide', game_text="This attack's damage isn't affected by Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_glaceon_5_speed_slide())])
