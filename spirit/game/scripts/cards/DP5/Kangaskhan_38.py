"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    multi_flip_damage,
)

card = PokemonCardDef(guid='dbfb0cfe-96dd-521b-a34f-5b6bfb1659bf', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name', display_name='Kangaskhan', searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'], subtypes=['Basic'], collector_number=38, set_code='DP5', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, family_id=115, abilities=[Attack(title='Bite', cost={PokemonTypes.COLORLESS: 2}, damage=30), Attack(title='Comet Punch', game_text='Flip 4 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 3}, damage=20, damage_operator='x', effect=multi_flip_damage(4, 20))])
