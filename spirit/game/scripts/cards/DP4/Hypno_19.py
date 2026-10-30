"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp4_hypno_19_dream_catcher,
)

card = PokemonCardDef(guid='3c38164c-ce55-5a58-ba64-2e46cf8bb2bd', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name', display_name='Hypno', searchable_by=['Hypno', 'Stage 1', 'Hypno'], subtypes=['Stage 1'], collector_number=19, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name', family_id=96, abilities=[Attack(title='Dream Catcher', game_text='If the Defending Pokémon is Asleep, move all damage counters from Hypno to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 2}, effect=dp4_hypno_19_dream_catcher()), Attack(title='Hypnoblast', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=condition_attack(SpecialConditions.ASLEEP))])
