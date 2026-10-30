"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    switch_self_attack,
)

card = PokemonCardDef(guid='72e20ccf-0db9-55b8-9d36-8a7fd4045bb4', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name', display_name='Spoink', searchable_by=['Spoink', 'Basic', 'Spoink'], subtypes=['Basic'], collector_number=121, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=325, abilities=[Attack(title='Psybeam', game_text='The Defending Pokémon is now Confused.', cost={PokemonTypes.PSYCHIC: 1}, effect=condition_attack(SpecialConditions.CONFUSED)), Attack(title='Bounce', game_text='You may switch Spoink with 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=switch_self_attack(damage=20, optional=True))])
