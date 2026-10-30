"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_piloswine_69_charge_dash,
)

card = PokemonCardDef(guid='2236b939-4240-5f29-a055-12fa03ad932d', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name', display_name='Piloswine', searchable_by=['Piloswine', 'Stage 1', 'Piloswine'], subtypes=['Stage 1'], collector_number=69, set_code='DP6', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.METAL, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name', family_id=220, abilities=[Attack(title='Charge Dash', game_text='You may do 30 damage plus 30 more damage. If you do, Piloswine does 30 damage to itself.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=dp6_piloswine_69_charge_dash()), Attack(title='Icy Wind', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3}, damage=60, effect=condition_attack(SpecialConditions.ASLEEP))])
