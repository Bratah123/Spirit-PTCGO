"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dp3_unownn_69_nod,
)

card = PokemonCardDef(guid='75aaf2c6-066a-5e46-a04e-8b0f7b17cc46', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownN.Name', display_name='Unown [N]', searchable_by=['Unown [N]', 'Basic', 'UnownN'], subtypes=['Basic'], collector_number=69, set_code='DP3', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='Nod', game_text="Once during your turn (before your attack), if you have Unown N, Unown O, and Unown D on your Bench, you may ask your opponent to take a Prize card. If he or she does, you take a Prize card. If he or she doesn't, draw a card.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_unownn_69_nod(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Flip a coin. If heads, the Defending Pokémon is now Burned.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.BURNED, flip=True))])
