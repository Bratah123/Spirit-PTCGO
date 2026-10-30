"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_pineco_113_selfdestruct,
)

card = PokemonCardDef(guid='b59ce4e3-34ca-5e8e-a907-e98ffc087f8f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name', display_name='Pineco', searchable_by=['Pineco', 'Basic', 'Pineco'], subtypes=['Basic'], collector_number=113, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=204, abilities=[Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Selfdestruct', game_text="This attack does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.) Pineco does 50 damage to itself.", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp6_pineco_113_selfdestruct())])
