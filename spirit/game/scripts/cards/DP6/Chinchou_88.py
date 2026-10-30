"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_chinchou_88_aqua_spark,
)

card = PokemonCardDef(guid='2b53406b-3285-5308-9014-ef31de96d919', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name', display_name='Chinchou', searchable_by=['Chinchou', 'Basic', 'Chinchou'], subtypes=['Basic'], collector_number=88, set_code='DP6', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=170, abilities=[Attack(title='Razor Fin', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Aqua Spark', game_text='If Chinchou has any Water Energy attached to it, this attack does 20 damage plus 10 more damage.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp6_chinchou_88_aqua_spark())])
