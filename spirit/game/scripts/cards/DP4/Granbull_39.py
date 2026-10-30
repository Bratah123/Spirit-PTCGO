"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import charm_reduce_defender_next
from spirit.game.card_effects.dp import (
    dp4_granbull_39_rage,
)

card = PokemonCardDef(guid='6031f5f2-f84a-567b-a34a-9002a3ca46e7', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name', display_name='Granbull', searchable_by=['Granbull', 'Stage 1', 'Granbull'], subtypes=['Stage 1'], collector_number=39, set_code='DP4', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name', family_id=209, abilities=[Attack(title='Daunt', game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 20 (before applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=charm_reduce_defender_next(20)), Attack(title='Rage', game_text='Does 40 damage plus 10 more damage for each damage counter on Granbull.', cost={PokemonTypes.COLORLESS: 4}, damage=40, damage_operator='+', effect=dp4_granbull_39_rage())])
