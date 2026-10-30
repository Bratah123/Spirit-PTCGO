"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_minun_32_minus_charge,
    dp3_minun_32_tag_play,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='8390795d-0fbf-524c-87b4-a85d48ace423', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name', display_name='Minun', searchable_by=['Minun', 'Basic', 'Minun'], subtypes=['Basic'], collector_number=32, set_code='DP3', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=312, abilities=[Ability(title='Minus Charge', game_text="Once during your turn (before your attack), if any Pokémon were Knocked Out during your opponent's last turn, you may draw 2 cards. You can't use more than 1 Minus Charge Poké-Power each turn. This power can't be used if Minun is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_minun_32_minus_charge(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Tag Play —', game_text='If you have Plusle on your Bench, you may move an Energy card attached to Minun to 1 of your Benched Pokémon.', cost={PokemonTypes.LIGHTNING: 1}, damage=20, effect=dp3_minun_32_tag_play())])
