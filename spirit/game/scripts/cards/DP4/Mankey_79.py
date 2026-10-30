"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_mankey_79_rage,
)

card = PokemonCardDef(guid='9574770f-e936-5b76-a99f-34530b4f2b6b', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name', display_name='Mankey', searchable_by=['Mankey', 'Basic', 'Mankey'], subtypes=['Basic'], collector_number=79, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=56, abilities=[Attack(title='Light Punch', cost={PokemonTypes.FIGHTING: 1}, damage=10), Attack(title='Rage', game_text='Does 10 damage plus 10 more damage for each damage counter on Mankey.', cost={PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=dp4_mankey_79_rage())])
