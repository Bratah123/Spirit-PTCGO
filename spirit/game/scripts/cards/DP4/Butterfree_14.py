"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp4_butterfree_14_parallel_drain,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='a89a1cd0-bb72-59dc-aaa9-efcc88bd86e5', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name', display_name='Butterfree', searchable_by=['Butterfree', 'Stage 2', 'Butterfree'], subtypes=['Stage 2'], collector_number=14, set_code='DP4', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name', family_id=10, abilities=[Attack(title='Parallel Drain', game_text='After your attack, remove from 1 of your Pokémon the number of damage counters equal to the damage you did to the Defending Pokémon.', cost={PokemonTypes.GRASS: 1}, damage=30, effect=dp4_butterfree_14_parallel_drain()), Attack(title='Dozing Scales', game_text='Flip a coin. If heads, the Defending Pokémon is now Asleep. If tails, the Defending Pokémon is now Poisoned.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=condition_attack(SpecialConditions.ASLEEP, flip=True))])
