"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.dp import (
    dp6_magnezonelvx_142_electric_trans,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='6d5fe875-7551-5ef8-b917-18078ccd2969', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneLVX.Name', display_name='Magnezone LV.X', searchable_by=['Magnezone LV.X', 'Level-Up', 'MagnezoneLVX'], subtypes=['Level-Up'], collector_number=142, set_code='DP6', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.METAL], stage=PokemonStage.LEVELUP, retreat_cost=4, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name', family_id=462, abilities=[Ability(title='Electric Trans', game_text="As often as you like during your turn (before your attack), you may move a Lightning or Metal Energy attached to 1 of your Pokémon to another of your Pokémon. This power can't be used if Magnezone is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_magnezonelvx_142_electric_trans(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Cyber Shock', game_text='Discard a Lightning Energy and a Metal Energy attached to Magnezone. The Defending Pokémon is now Paralyzed.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1}, damage=80, effect=condition_attack(SpecialConditions.PARALYZED))])
