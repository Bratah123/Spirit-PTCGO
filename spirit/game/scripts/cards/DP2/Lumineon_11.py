"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    lure_ring_gust_hp,
    reverse_stream,
)
from spirit.game.card_effects.ex import is_active_pokemon

card = PokemonCardDef(guid='f74fc884-812f-5738-9faa-cea179eeb0b3', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name', display_name='Lumineon', searchable_by=['Lumineon', 'Stage 1', 'Lumineon'], subtypes=['Stage 1'], collector_number=11, set_code='DP2', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name', family_id=456, abilities=[Ability(title='Lure Ring', game_text="Once during your turn (before your attack), if Lumineon is your Active Pokémon, you may choose 1 of your opponent's Benched Pokémon that has a maximum HP of 100 or more and switch it with 1 of the Defending Pokémon. This power can't be used if Lumineon is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=lure_ring_gust_hp(100), activation=Activations.ONCE_PER_TURN, condition=is_active_pokemon), Attack(title='Reverse Stream', game_text='Does 30 damage plus 10 more damage for each Water Energy attached to Lumineon. Then, return all Water Energy attached to Lumineon to your hand.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='+', effect=reverse_stream(30, 10))])
