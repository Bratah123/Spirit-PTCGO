"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_combusken_35_bulk_up,
    multi_flip_damage,
)

card = PokemonCardDef(guid='94d9699c-e1e6-5f18-ac86-a82afbe0a9ae', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name', display_name='Combusken', searchable_by=['Combusken', 'Stage 1', 'Combusken'], subtypes=['Stage 1'], collector_number=35, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name', family_id=255, abilities=[Attack(title='Bulk Up', game_text="During your next turn, each of Combusken's attacks does 30 more damage to the Defending Pokémon (before applying Weakness and Resistance).", cost={PokemonTypes.FIRE: 1}, damage=30, effect=dp4_combusken_35_bulk_up()), Attack(title='Double Kick', game_text='Flip 2 coins. This attack does 50 damage times the number of heads.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='x', effect=multi_flip_damage(2, 50))])
