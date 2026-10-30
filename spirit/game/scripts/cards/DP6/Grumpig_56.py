"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_grumpig_56_grind,
    dp6_grumpig_56_magical_step,
)

card = PokemonCardDef(guid='420dd2c1-f8a3-50ce-87a0-5f8f56a5da1f', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name', display_name='Grumpig', searchable_by=['Grumpig', 'Stage 1', 'Grumpig'], subtypes=['Stage 1'], collector_number=56, set_code='DP6', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name', family_id=325, abilities=[Attack(title='Magical Step', game_text='The Defending Pokémon is now Confused. Put 6 damage counters instead of 3 on the Confused Pokémon.', cost={}, effect=dp6_grumpig_56_magical_step()), Attack(title='Grind', game_text='Does 20 damage times the amount of Energy attached to Grumpig.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=dp6_grumpig_56_grind())])
