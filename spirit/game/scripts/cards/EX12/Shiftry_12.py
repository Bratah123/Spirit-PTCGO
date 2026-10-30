"""STUB: effect not implemented — do not guess mechanics.
Shiftry (EX12 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    cross_cut_evolved,
    evolutionary_fan_devolve,
    reactive_beating_confuse,
)

card = PokemonCardDef(guid='8c2e911a-edcb-5756-93d4-cd7a10745918', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name', display_name='Shiftry', searchable_by=['Shiftry', 'Stage 2', 'Shiftry'], subtypes=['Stage 2'], collector_number=12, set_code='EX12', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name', family_id=273, abilities=[Ability(title='Evolutionary Fan', game_text='Once during your turn, when you play Shiftry from your hand to evolve 1 of your Pokémon, you may choose 1 of your Evolved Pokémon in play (excluding any Shiftry). Return that Pokémon and all cards attached to it to your hand.', ability_type=AbilityTypes.POKE_POWER, effect=evolutionary_fan_devolve(), trigger=Triggers.ON_EVOLVE), Attack(title='Reactive Beating', game_text='If Shiftry has any React Energy cards attached to it, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=reactive_beating_confuse(30)), Attack(title='Cross-Cut', game_text='If the Defending Pokémon is an Evolved Pokémon, this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=cross_cut_evolved(40, 30))])
