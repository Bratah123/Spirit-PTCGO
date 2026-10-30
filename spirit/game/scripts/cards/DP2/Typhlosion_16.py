"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    firestarter,
)
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='f100fed8-0449-5837-9a41-0b57efecb6a9', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name', display_name='Typhlosion', searchable_by=['Typhlosion', 'Stage 2', 'Typhlosion'], subtypes=['Stage 2'], collector_number=16, set_code='DP2', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name', family_id=155, abilities=[Ability(title='Firestarter', game_text="Once during your turn (before your attack), you may attach a Fire Energy card from your discard pile to 1 of your Benched Pokémon. This power can't be used if Typhlosion is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=firestarter(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Evaporating Heat', game_text='Discard a Water Energy attached to the Defending Pokémon.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=discard_opponent_energy_attack(count=1))])
