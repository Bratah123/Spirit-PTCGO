"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_plusle_36_plus_charge,
    dp3_plusle_36_tag_play,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='6da4c313-3e93-5221-8cdc-e99c739c31ac', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name', display_name='Plusle', searchable_by=['Plusle', 'Basic', 'Plusle'], subtypes=['Basic'], collector_number=36, set_code='DP3', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=311, abilities=[Ability(title='Plus Charge', game_text="Once during your turn (before your attack), if any of your Pokémon were Knocked Out during your opponent's last turn, you may search your discard pile for up to 2 basic Energy cards, show them to your opponent, and put them into your hand. You can't use more than 1 Plus Charge Poké-Power each turn. This power can't be used if Plusle is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_plusle_36_plus_charge(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Tag Play +', game_text="If you have Minun on your Bench, you may do 20 damage to any 1 Benched Pokémon instead. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1}, damage=20, effect=dp3_plusle_36_tag_play())])
