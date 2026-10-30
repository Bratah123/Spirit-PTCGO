"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.dp import (
    evolution_impulse_search,
)

card = PokemonCardDef(guid='4ac83ce2-c11b-5521-8c11-64efb8453f1f', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name', display_name='Bayleef', searchable_by=['Bayleef', 'Stage 1', 'Bayleef'], subtypes=['Stage 1'], collector_number=41, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name', family_id=152, abilities=[Attack(title='Evolution Impulse', game_text='Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=evolution_impulse_search()), Attack(title='Leaf Boomerang', game_text='Flip 2 coins. This attack does 30 damage times the number of heads.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='x', effect=flip_damage(coins=2, per_heads=30))])
