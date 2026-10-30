"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    flame_bluster_snipe,
    torrid_wave_burn,
)
from spirit.game.card_effects.ex import is_active_pokemon

card = PokemonCardDef(guid='ea5fc6a9-40a8-511a-9344-c1fb60c2d6b7', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.MagmortarLVX.Name', display_name='Magmortar LV.X', searchable_by=['Magmortar LV.X', 'Level-Up', 'MagmortarLVX'], subtypes=['Level-Up'], collector_number=123, set_code='DP2', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.FIRE], stage=PokemonStage.LEVELUP, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name', family_id=126, abilities=[Ability(title='Torrid Wave', game_text="Once during your turn (before your attack), if Magmortar is your Active Pokémon, you may choose 1 of the Defending Pokémon. That Pokémon is now Burned. Put 3 damage counters instead of 2 on that Pokémon between turns. This power can't be used if Magmortar is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=torrid_wave_burn(), activation=Activations.ONCE_PER_TURN, condition=is_active_pokemon), Attack(title='Flame Bluster', game_text="Discard 2 Fire Energy attached to Magmortar. Choose 1 of your opponent's Pokémon. This attack does 100 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) During your next turn, Magmortar can't use Flame Bluster.", cost={PokemonTypes.FIRE: 4}, effect=flame_bluster_snipe(40, 2))])
