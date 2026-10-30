"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    hide_crowd,
    swarm_count_murkrow,
)

card = PokemonCardDef(guid='82c9c267-37f2-55f3-9567-2737542b0e44', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name', display_name='Murkrow', searchable_by=['Murkrow', 'Basic', 'Murkrow'], subtypes=['Basic'], collector_number=90, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=198, abilities=[Attack(title='Swarm', game_text='Search your deck for Murkrow and put it onto your Bench. Shuffle your deck afterward.', cost={}, effect=swarm_count_murkrow()), Attack(title='Hide Crowd', game_text='Switch Murkrow with 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=hide_crowd(20))])
