"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_groudon_29_drought,
    dp6_groudon_29_major_earthquake,
)

card = PokemonCardDef(guid='7dda3882-d47d-5e6b-aa9b-b233c7e553b6', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name', display_name='Groudon', searchable_by=['Groudon', 'Basic', 'Groudon'], subtypes=['Basic'], collector_number=29, set_code='DP6', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=383, abilities=[Attack(title='Drought', game_text='Choose up to 2 basic Fighting Energy cards from your hand and attach them to 1 of your Pokémon.', cost={}, effect=dp6_groudon_29_drought()), Attack(title='Major Earthquake', game_text="Discard 2 Fighting Energy attached to Groudon and this attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=dp6_groudon_29_major_earthquake())])
