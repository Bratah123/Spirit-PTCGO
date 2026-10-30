"""STUB: effect not implemented — do not guess mechanics.
Flygon ex (EX12 #87): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    emerge_charge_on_evolve,
    reactive_blast,
)

card = PokemonCardDef(guid='21694fe4-a170-5ac3-95b0-baae1f1d699e', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Flygonex.Name', display_name='Flygon ex', searchable_by=['Flygon ex', 'Stage 2', 'ex', 'Flygonex'], subtypes=['Stage 2', 'ex'], collector_number=87, set_code='EX12', rarity=Rarities.RareHoloEX, hp=150, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name', family_id=328, abilities=[Ability(title='Emerge Charge', game_text='Once during your turn, when you play Flygon ex from your hand to evolve 1 of your Pokémon, you may search your discard pile for up to 2 Energy cards and attach them to Flygon ex.', ability_type=AbilityTypes.POKE_POWER, effect=emerge_charge_on_evolve(2), trigger=Triggers.ON_EVOLVE), Attack(title='Reactive Blast', game_text='You may discard any number of React Energy cards attached to Flygon ex. If you do, this attack does 40 damage plus 30 more damage for each Energy card you discarded.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=reactive_blast(40, 30)), Attack(title='Dragon Claw', cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3}, damage=100)])
