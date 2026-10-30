"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_zangoose_59_cutting_claw,
)

card = PokemonCardDef(guid='f31247ad-1f3c-5061-b82b-76a1ff11ffb7', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name', display_name='Zangoose', searchable_by=['Zangoose', 'Basic', 'Zangoose'], subtypes=['Basic'], collector_number=59, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=335, abilities=[Attack(title='Slash', cost={PokemonTypes.COLORLESS: 1}, damage=20), Attack(title='Cutting Claw', game_text='If your opponent has Seviper in play, this attack does 40 damage plus 50 more damage.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=dp4_zangoose_59_cutting_claw())])
