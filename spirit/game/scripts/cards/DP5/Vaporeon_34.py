"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_vaporeon_34_cleanse_away,
    dp5_vaporeon_34_hyper_whirlpool,
)

card = PokemonCardDef(guid='5efa2d3a-7d55-52bc-bc03-db89ed990e36', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name', display_name='Vaporeon', searchable_by=['Vaporeon', 'Stage 1', 'Vaporeon'], subtypes=['Stage 1'], collector_number=34, set_code='DP5', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Attack(title='Cleanse Away', game_text='Remove 2 damage counters from each of your Benched Pokémon.', cost={PokemonTypes.WATER: 1}, damage=30, effect=dp5_vaporeon_34_cleanse_away()), Attack(title='Hyper Whirlpool', game_text='Flip a coin until you get tails. For each heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_vaporeon_34_hyper_whirlpool())])
