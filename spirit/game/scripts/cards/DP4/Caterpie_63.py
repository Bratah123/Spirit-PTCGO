"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_caterpie_63_pupate,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='70d1acbd-315c-579a-9237-c257a54cc366', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name', display_name='Caterpie', searchable_by=['Caterpie', 'Basic', 'Caterpie'], subtypes=['Basic'], collector_number=63, set_code='DP4', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=10, abilities=[Ability(title='Pupate', game_text="Once during your turn (before your attack), if Caterpie is your Active Pokémon, you may flip a coin. If heads, search your deck for a card that evolves from Caterpie and put it onto Caterpie. (This counts as evolving Caterpie.) Shuffle your deck afterward. This power can't be used if Caterpie is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_caterpie_63_pupate(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Tackle', cost={PokemonTypes.GRASS: 1}, damage=20)])
