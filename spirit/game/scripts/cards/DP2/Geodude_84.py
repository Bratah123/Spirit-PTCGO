"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    stone_throw_snipe,
)

card = PokemonCardDef(guid='2bbe5fe0-e593-56eb-9183-b339c02a6a36', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name', display_name='Geodude', searchable_by=['Geodude', 'Basic', 'Geodude'], subtypes=['Basic'], collector_number=84, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, family_id=74, abilities=[Attack(title='Stone Throw', game_text="Choose 2 of your opponent's Benched Pokémon. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1}, effect=stone_throw_snipe(10, 2))])
