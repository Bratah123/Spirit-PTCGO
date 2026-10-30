"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    miracle_oracle,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='5c6b344c-61d6-570c-9aae-edf71004baeb', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name', display_name='Bronzong', searchable_by=['Bronzong', 'Stage 1', 'Bronzong'], subtypes=['Stage 1'], collector_number=6, set_code='DP2', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name', family_id=436, abilities=[Ability(title='Miracle Oracle', game_text="Once during your turn (before your attack), you may draw a card. Then, discard a card from your hand. If you discard an Energy card, draw 1 more card. This power can't be used if Bronzong is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=miracle_oracle(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Shady Stamp', game_text='The Defending Pokémon is now Confused.', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=condition_attack(SpecialConditions.CONFUSED))])
