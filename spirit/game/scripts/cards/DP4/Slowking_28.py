"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp4_slowking_28_psych_up,
    dp4_slowking_28_trump_card,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='9a001a18-aa05-5180-802b-f331b10f0443', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name', display_name='Slowking', searchable_by=['Slowking', 'Stage 1', 'Slowking'], subtypes=['Stage 1'], collector_number=28, set_code='DP4', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name', family_id=79, abilities=[Ability(title='Trump Card', game_text="Once during your turn (before your attack), if any of your Pokémon were Knocked Out during your opponent's last turn, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward. This power can't be used if Slowking is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp4_slowking_28_trump_card(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Psych Up', game_text="During your next turn, Slowking's Psych Up attack's base damage is 60.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=dp4_slowking_28_psych_up())])
