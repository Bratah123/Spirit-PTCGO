"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_gardevoirlvx_131_bring_down,
    dp3_gardevoirlvx_131_teleportation,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='cd22cd11-0690-5974-a263-77ad70017a8e', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirLVX.Name', display_name='Gardevoir LV.X', searchable_by=['Gardevoir LV.X', 'Level-Up', 'GardevoirLVX'], subtypes=['Level-Up'], collector_number=131, set_code='DP3', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.LEVELUP, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name', family_id=280, abilities=[Ability(title='Teleportation', game_text="Once during your turn (before your attack), choose 1 of your Active Pokémon or 1 or your Benched Pokémon and switch Gardevoir with that Pokémon. This power can't be used if Gardevoir is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_gardevoirlvx_131_teleportation(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Bring Down', game_text="Choose 1 Pokémon (yours or your opponent's) with the fewest remaining HP (excluding Gardevoir) and that Pokémon is now Knocked Out.", cost={PokemonTypes.PSYCHIC: 2}, effect=dp3_gardevoirlvx_131_bring_down())])
