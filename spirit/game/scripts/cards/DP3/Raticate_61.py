"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_raticate_61_gnaw_off,
    dp3_raticate_61_sneaky_attack,
)

card = PokemonCardDef(guid='29fd30f7-87db-5b39-805d-ec6a910e27ec', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name', display_name='Raticate', searchable_by=['Raticate', 'Stage 1', 'Raticate'], subtypes=['Stage 1'], collector_number=61, set_code='DP3', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name', family_id=19, abilities=[Attack(title='Gnaw Off', game_text='Flip a coin. If heads, this attack does 10 damage plus 60 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp3_raticate_61_gnaw_off()), Attack(title='Sneaky Attack', game_text='If Raticate has any Darkness Energy attached to it, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp3_raticate_61_sneaky_attack())])
