"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_donphan_48_bash_in,
    dp3_donphan_48_rapid_spin,
)

card = PokemonCardDef(guid='79139eda-c8c7-5606-b1d8-40e140d3699b', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name', display_name='Donphan', searchable_by=['Donphan', 'Stage 1', 'Donphan'], subtypes=['Stage 1'], collector_number=48, set_code='DP3', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name', family_id=231, abilities=[Attack(title='Rapid Spin', game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon, if any. You switch Donphan with 1 of your Benched Pokémon, if any.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp3_donphan_48_rapid_spin()), Attack(title='Bash In', game_text='If the Defending Pokémon has a Pokémon Tool card attached to it, this attack does 70 damage plus 60 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2}, damage=70, damage_operator='+', effect=dp3_donphan_48_bash_in())])
