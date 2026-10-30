"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_togetic_55_sweet_kiss,
)

card = PokemonCardDef(guid='4c78d5a2-fb99-512a-b72a-8240fb81f1c8', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name', display_name='Togetic', searchable_by=['Togetic', 'Stage 1', 'Togetic'], subtypes=['Stage 1'], collector_number=55, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name', family_id=175, abilities=[Attack(title='Speed Dive', cost={PokemonTypes.COLORLESS: 2}, damage=20), Attack(title='Sweet Kiss', game_text='Your opponent may draw a card.', cost={PokemonTypes.COLORLESS: 3}, damage=50, effect=dp4_togetic_55_sweet_kiss())])
