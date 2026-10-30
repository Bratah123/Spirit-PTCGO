"""STUB: effect not implemented — do not guess mechanics.
Magneton (EX12 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    multiple_force,
    reactive_recharge_on_ko,
)

card = PokemonCardDef(guid='225ad915-39c4-5128-9296-a3e69ab564d4', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name', display_name='Magneton', searchable_by=['Magneton', 'Stage 1', 'Magneton'], subtypes=['Stage 1'], collector_number=22, set_code='EX12', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name', family_id=81, abilities=[Ability(title='Reactive Recharge', game_text="If Magneton would be Knocked Out by damage from an opponent's attack, you may move any number of React Energy cards from Magneton to your Pokémon in any way you like.", ability_type=AbilityTypes.POKE_POWER, effect=reactive_recharge_on_ko(), trigger=Triggers.ON_KNOCKED_OUT), Attack(title='Multiple Force', game_text="If Magneton has any React Energy cards attached to it, this attack does 30 damage plus 10 more damage for each Magnemite and Magneton (both yours and your opponent's) in play.", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=multiple_force(30, 10)), Attack(title='Magnetic Blast', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3}, damage=60)])
