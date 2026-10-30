"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_spinda_111_dish_out,
    dp3_spinda_111_synchro_punch,
)

card = PokemonCardDef(guid='85aabf04-f1f6-581b-a034-52fe898c7baf', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name', display_name='Spinda', searchable_by=['Spinda', 'Basic', 'Spinda'], subtypes=['Basic'], collector_number=111, set_code='DP3', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=327, abilities=[Attack(title='Dish Out', game_text='Draw a card from the top and the bottom of your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_spinda_111_dish_out()), Attack(title='Synchro Punch', game_text='If any basic Energy card attached to Spinda is the same type as any Energy attached to the Defending Pokémon, this attack does 10 damage plus 30 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp3_spinda_111_synchro_punch())])
