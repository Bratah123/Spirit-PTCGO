"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_lanturn_58_rushing_water,
)

card = PokemonCardDef(guid='c07e5f4d-d713-5086-a00d-7055a0999e6e', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name', display_name='Lanturn', searchable_by=['Lanturn', 'Stage 1', 'Lanturn'], subtypes=['Stage 1'], collector_number=58, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name', family_id=170, abilities=[Attack(title='Rushing Water', game_text="Move an Energy card attached to the Defending Pokémon to another of your opponent's Pokémon.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp6_lanturn_58_rushing_water()), Attack(title='Confuse Ray', game_text='The Defending Pokémon is now Confused.', cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1}, damage=40, effect=condition_attack(SpecialConditions.CONFUSED))])
