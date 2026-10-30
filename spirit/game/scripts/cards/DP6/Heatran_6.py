"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_heatran_6_flash_fire,
    dp6_heatran_6_magma_storm,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='4b4c00b5-4d8b-5afc-a450-a4ef7501e1fd', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name', display_name='Heatran', searchable_by=['Heatran', 'Basic', 'Heatran'], subtypes=['Basic'], collector_number=6, set_code='DP6', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.WATER, family_id=485, abilities=[Ability(title='Flash Fire', game_text="Once during your turn (before your attack), you may move a Fire Energy attached to 1 of your Pokémon to Heatran. This power can't be used if Heatran is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_heatran_6_flash_fire(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Magma Storm', game_text='You may discard as many basic Energy cards as you like attached to Heatran. If you do, this attack does 40 damage plus 20 more damage for each Energy card you discarded.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=dp6_heatran_6_magma_storm())])
