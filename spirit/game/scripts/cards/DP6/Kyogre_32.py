"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_kyogre_32_drizzle,
    dp6_kyogre_32_high_tide,
)

card = PokemonCardDef(guid='46403c79-6dae-5bfd-afc7-46306ff2d796', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name', display_name='Kyogre', searchable_by=['Kyogre', 'Basic', 'Kyogre'], subtypes=['Basic'], collector_number=32, set_code='DP6', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, family_id=382, abilities=[Attack(title='Drizzle', game_text='Choose up to 2 basic Water Energy cards from your hand and attach them to 1 of your Pokémon.', cost={}, effect=dp6_kyogre_32_drizzle()), Attack(title='High Tide', game_text="Discard 2 Water Energy attached to Kyogre. This attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp6_kyogre_32_high_tide())])
