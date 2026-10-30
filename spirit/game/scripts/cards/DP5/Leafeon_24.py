"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp4_sceptile_8_leaf_blade
from spirit.game.card_effects.dp import (
    heal_attack,
)

card = PokemonCardDef(guid='8c3fac4e-1a5f-5498-9ac3-7f1926674684', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name', display_name='Leafeon', searchable_by=['Leafeon', 'Stage 1', 'Leafeon'], subtypes=['Stage 1'], collector_number=24, set_code='DP5', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Attack(title='Sprial Drain', game_text='Remove 1 damage counter from Leafeon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=heal_attack(10)), Attack(title='Leaf Blade', game_text='Flip a coin. If heads, this attack does 50 damage plus 20 more damage.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp4_sceptile_8_leaf_blade())])
