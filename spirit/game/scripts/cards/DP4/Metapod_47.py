"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_metapod_47_emerge,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='7a59172b-2346-5507-8908-c48a172abb48', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name', display_name='Metapod', searchable_by=['Metapod', 'Stage 1', 'Metapod'], subtypes=['Stage 1'], collector_number=47, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name', family_id=10, abilities=[Ability(title='Emerge', game_text="Once during your turn (before your attack), if Metapod is your Active Pokémon, you may flip a coin. If heads, search your deck for a card that evolves from Metapod and put it onto Metapod. (This counts as evolving Metapod.) Shuffle your deck afterward. This power can't be used if Metapod is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_metapod_47_emerge(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Ram', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30)])
