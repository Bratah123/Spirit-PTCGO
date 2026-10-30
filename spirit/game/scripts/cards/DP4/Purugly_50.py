"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import may_discard_defender_energy_on_heads
from spirit.game.card_effects.dp import (
    multi_flip_damage,
)

card = PokemonCardDef(guid='9e85ec5b-ecd1-57fc-a1e6-6399b576ffff', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name', display_name='Purugly', searchable_by=['Purugly', 'Stage 1', 'Purugly'], subtypes=['Stage 1'], collector_number=50, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name', family_id=431, abilities=[Attack(title='Swagger', game_text='Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=may_discard_defender_energy_on_heads()), Attack(title='Fury Swipes', game_text='Flip 3 coins. This attack does 40 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='x', effect=multi_flip_damage(3, 40))])
