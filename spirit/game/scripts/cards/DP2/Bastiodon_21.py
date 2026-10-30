"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    anger_revenge,
    protective_wall_passive,
)

card = PokemonCardDef(guid='5a25c9f1-d396-52f3-919d-03b23ecef0b5', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name', display_name='Bastiodon', searchable_by=['Bastiodon', 'Stage 2', 'Bastiodon'], subtypes=['Stage 2'], collector_number=21, set_code='DP2', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name', family_id=410, abilities=[Ability(title='Protective Wall', game_text="Prevent all damage done to your Benched Pokémon by your opponent's attacks.", ability_type=AbilityTypes.POKE_BODY, passive=protective_wall_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Anger Revenge', game_text="If Bastiodon was damaged by an attack during your opponent's last turn, this attack does 40 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=anger_revenge(60, 2))])
