"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_glameow_68_captivate,
)

card = PokemonCardDef(guid='b81f0063-dee8-56f9-bd45-410b630a6365', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name', display_name='Glameow', searchable_by=['Glameow', 'Basic', 'Glameow'], subtypes=['Basic'], collector_number=68, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=431, abilities=[Attack(title='Captivate', game_text="Switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=dp4_glameow_68_captivate()), Attack(title='Slash', cost={PokemonTypes.COLORLESS: 2}, damage=20)])
