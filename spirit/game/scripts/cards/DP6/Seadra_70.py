"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_seadra_70_aqua_pump,
)

card = PokemonCardDef(guid='9499c4ad-11fa-531e-99f8-6cfcef5899aa', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name', display_name='Seadra', searchable_by=['Seadra', 'Stage 1', 'Seadra'], subtypes=['Stage 1'], collector_number=70, set_code='DP6', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name', family_id=116, abilities=[Attack(title='Aqua Pump', game_text='You may discard up to 2 Water Energy cards from your hand. If you do, this attack does 30 damage plus 10 more damage for each Energy card you discarded.', cost={PokemonTypes.WATER: 1}, damage=30, damage_operator='+', effect=dp6_seadra_70_aqua_pump()), Attack(title='Waterfall', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=50)])
