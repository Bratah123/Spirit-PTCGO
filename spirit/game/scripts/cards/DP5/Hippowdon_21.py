"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_hippowdon_21_sand_impact,
    dp5_hippowdon_21_vacuum_sand,
)

card = PokemonCardDef(guid='0f170898-8eef-5dc0-9baa-262c832f9226', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name', display_name='Hippowdon', searchable_by=['Hippowdon', 'Stage 1', 'Hippowdon'], subtypes=['Stage 1'], collector_number=21, set_code='DP5', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name', family_id=449, abilities=[Attack(title='Vacuum Sand', game_text='Search your discard pile for a Fighting Energy card and attach it to Hippowdon.', cost={}, damage=20, effect=dp5_hippowdon_21_vacuum_sand()), Attack(title='Sand Impact', game_text='Flip a coin for each Fighting Energy attached to Hippowdon. This attack does 50 damage plus 20 more damage for each heads.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp5_hippowdon_21_sand_impact())])
