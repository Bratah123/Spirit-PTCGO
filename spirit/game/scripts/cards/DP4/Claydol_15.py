"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_claydol_15_cosmic_power,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='3f365b4b-3e10-569e-8a0b-d9752d4658cb', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name', display_name='Claydol', searchable_by=['Claydol', 'Stage 1', 'Claydol'], subtypes=['Stage 1'], collector_number=15, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name', family_id=343, abilities=[Ability(title='Cosmic Power', game_text="Once during your turn (before your attack), you may choose up to 2 cards from your hand and put them on the bottom of your deck in any order. If you do, draw cards until you have 6 cards in your hand. This power can't be used if Claydol is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_claydol_15_cosmic_power(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Spinning Attack', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40)])
