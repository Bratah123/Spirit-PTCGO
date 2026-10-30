"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_miltank_55_continuous_tumble,
    dp3_miltank_55_healing_milk,
)

card = PokemonCardDef(guid='7fa91a3e-950f-5bb5-bf90-24e7d56e96b3', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name', display_name='Miltank', searchable_by=['Miltank', 'Basic', 'Miltank'], subtypes=['Basic'], collector_number=55, set_code='DP3', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=241, abilities=[Attack(title='Healing Milk', game_text='Flip 2 coins. For each heads, remove 3 damage counters from 1 of your Pokémon.', cost={}, effect=dp3_miltank_55_healing_milk()), Attack(title='Continuous Tumble', game_text='Flip a coin until you get tails. This attack does 20 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=dp3_miltank_55_continuous_tumble())])
