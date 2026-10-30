"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_taillow_124_focus_energy,
)

card = PokemonCardDef(guid='d29f8585-c8e4-5803-87ef-5aedf211dd3c', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name', display_name='Taillow', searchable_by=['Taillow', 'Basic', 'Taillow'], subtypes=['Basic'], collector_number=124, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=276, abilities=[Attack(title='Focus Energy', game_text="During your next turn, Taillow's Peck attack's base damage is 30.", cost={PokemonTypes.COLORLESS: 1}, effect=dp6_taillow_124_focus_energy()), Attack(title='Peck', cost={PokemonTypes.COLORLESS: 1}, damage=10)])
