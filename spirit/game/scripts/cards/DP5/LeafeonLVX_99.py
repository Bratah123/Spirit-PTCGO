"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_leafeonlvx_99_energy_forcing,
    dp5_leafeonlvx_99_verdant_dance,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='6360b467-f0e9-5aba-9727-e5bb5822c7c0', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonLVX.Name', display_name='Leafeon LV.X', searchable_by=['Leafeon LV.X', 'Level-Up', 'LeafeonLVX'], subtypes=['Level-Up'], collector_number=99, set_code='DP5', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.GRASS], stage=PokemonStage.LEVELUP, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name', family_id=133, abilities=[Ability(title='Energy Forcing', game_text="Once during your turn (before your attack), you may attach an Energy card from your hand to 1 of your Pokémon. This power can't be used if Leafeon is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp5_leafeonlvx_99_energy_forcing(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Verdant Dance', game_text='Does 30 damage plus 10 more damage for each Energy attached to all of your Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=dp5_leafeonlvx_99_verdant_dance())])
