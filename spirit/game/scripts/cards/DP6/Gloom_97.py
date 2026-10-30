"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp6_gloom_97_space_out,
)

card = PokemonCardDef(guid='f28638cd-3b82-5548-99f2-ca7799494a6b', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name', display_name='Gloom', searchable_by=['Gloom', 'Stage 1', 'Gloom'], subtypes=['Stage 1'], collector_number=97, set_code='DP6', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name', family_id=43, abilities=[Attack(title='Space Out', game_text='Remove 2 damage counters from Gloom. Gloom is now Asleep.', cost={}, effect=dp6_gloom_97_space_out()), Attack(title='Stinky Nectar', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused and Poisoned.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
