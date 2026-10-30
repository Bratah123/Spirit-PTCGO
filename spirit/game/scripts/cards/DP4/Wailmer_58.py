"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_wailmer_58_tsunami,
)

card = PokemonCardDef(guid='28135d86-0f4a-5da5-86cc-6f8f2dd60f43', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name', display_name='Wailmer', searchable_by=['Wailmer', 'Basic', 'Wailmer'], subtypes=['Basic'], collector_number=58, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, family_id=320, abilities=[Attack(title='Tsunami', game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=10, effect=dp4_wailmer_58_tsunami()), Attack(title='Ram', cost={PokemonTypes.COLORLESS: 3}, damage=30)])
