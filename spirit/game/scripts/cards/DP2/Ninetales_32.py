"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    color_shift, poke_power_condition,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(guid='7c9fa3a8-d315-5ad2-875c-ce16aa72096f', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name', display_name='Ninetales', searchable_by=['Ninetales', 'Stage 1', 'Ninetales'], subtypes=['Stage 1'], collector_number=32, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name', family_id=37, abilities=[Ability(title='Color Shift', game_text="Once during your turn (before your attack), you may choose 1 of your opponent's Pokémon. Ninetales is the same type as that Pokémon (all if that Pokémon is more than 1 type) until the end of your turn. This power can't be used if Ninetales is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=color_shift(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Fire Blast', game_text='Discard a Fire Energy attached to Ninetales.', cost={PokemonTypes.FIRE: 2}, damage=60, effect=self_energy_discard_attack(count=1, then_damage=60))])
