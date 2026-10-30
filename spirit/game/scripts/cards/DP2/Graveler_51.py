"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiral_rush
from spirit.game.card_effects.dp import (
    rock_slide_bench,
)

card = PokemonCardDef(guid='0cf55a42-2fbb-56b1-b04f-7785bb414152', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name', display_name='Graveler', searchable_by=['Graveler', 'Stage 1', 'Graveler'], subtypes=['Stage 1'], collector_number=51, set_code='DP2', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.GRASS, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name', family_id=74, abilities=[Attack(title='Rock Cannon', game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='x', effect=spiral_rush()), Attack(title='Rock Slide', game_text="Does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=rock_slide_bench(40, 20))])
