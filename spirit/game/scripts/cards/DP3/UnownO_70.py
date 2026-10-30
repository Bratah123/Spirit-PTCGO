"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_unowno_70_one,
)

card = PokemonCardDef(guid='bd2e8b92-89f9-5e23-a7b6-0a789ace4113', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownO.Name', display_name='Unown [O]', searchable_by=['Unown [O]', 'Basic', 'UnownO'], subtypes=['Basic'], collector_number=70, set_code='DP3', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='ONE', game_text='Once during your turn (before your attack), if you have Unown O, Unown N, and Unown E on your Bench and you have 1 card left in your hand, you may draw cards until you have 7 cards in your hand.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_unowno_70_one(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Flip a coin. If heads, the Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.ASLEEP, flip=True))])
