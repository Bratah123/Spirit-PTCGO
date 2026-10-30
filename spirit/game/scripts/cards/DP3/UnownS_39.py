"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_unowns_39_set,
)

card = PokemonCardDef(guid='e148fcce-8a97-5389-becf-88383d24b199', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownS.Name', display_name='Unown [S]', searchable_by=['Unown [S]', 'Basic', 'UnownS'], subtypes=['Basic'], collector_number=39, set_code='DP3', rarity=Rarities.Rare, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='Set', game_text='Once during your turn (before your attack), if you have Unown S, Unown E, and Unown T on your Bench, you may flip a coin. If heads, search your discard pile for an Energy card, show it to your opponent, and put it on top of your deck.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_unowns_39_set(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.CONFUSED, flip=True))])
