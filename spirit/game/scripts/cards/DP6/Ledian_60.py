"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import multi_flip_damage
from spirit.game.card_effects.dp import (
    dp6_ledian_60_baton_pass,
)

card = PokemonCardDef(guid='870af73b-8933-5c8a-84cd-6c8f47d0fb76', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name', display_name='Ledian', searchable_by=['Ledian', 'Stage 1', 'Ledian'], subtypes=['Stage 1'], collector_number=60, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name', family_id=165, abilities=[Attack(title='Comet Punch', game_text='Flip 4 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=multi_flip_damage(4, 20)), Attack(title='Baton Pass', game_text='You may switch Ledian with 1 of your Benched Pokémon. If you do, move as many Energy cards attached to Ledian as you like to the new Active Pokémon.', cost={PokemonTypes.GRASS: 2}, damage=50, effect=dp6_ledian_60_baton_pass())])
