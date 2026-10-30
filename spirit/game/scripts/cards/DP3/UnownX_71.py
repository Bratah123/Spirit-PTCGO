"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_unownx_71_x_ray,
)

card = PokemonCardDef(guid='b338ecd6-5241-51ef-a7d7-52135c760fc7', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownX.Name', display_name='Unown [X]', searchable_by=['Unown [X]', 'Basic', 'UnownX'], subtypes=['Basic'], collector_number=71, set_code='DP3', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='X-RAY', game_text="Once during your turn (before your attack), if you have Unown X on your Bench, you may look at the top card of your opponent's deck and put it back on top of his or her deck.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_unownx_71_x_ray(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
