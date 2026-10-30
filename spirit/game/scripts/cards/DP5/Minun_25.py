"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_minun_25_spark,
)

card = PokemonCardDef(guid='e420174f-c5ed-5873-a669-da8a21f7014f', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name', display_name='Minun', searchable_by=['Minun', 'Basic', 'Minun'], subtypes=['Basic'], collector_number=25, set_code='DP5', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=312, abilities=[Attack(title='Pound', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='(+) Spark', game_text="If Plusle is on your Bench, this attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp5_minun_25_spark())])
