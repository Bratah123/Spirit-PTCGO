"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_electrode_26_energy_shift,
    dp3_electrode_26_ion_blast,
)

card = PokemonCardDef(guid='54d63347-2ff7-532b-b6f8-89943dc9e962', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name', display_name='Electrode', searchable_by=['Electrode', 'Stage 1', 'Electrode'], subtypes=['Stage 1'], collector_number=26, set_code='DP3', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', family_id=100, abilities=[Ability(title='Energy Shift', game_text="Once during your turn, if Electrode would be Knocked Out by damage from an attack, you may use this power. Electrode isn't discarded. Instead, attach it as an Energy card to 1 of your Pokémon. While attached, this card is a Special Energy card and provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.)", ability_type=AbilityTypes.POKE_POWER, effect=dp3_electrode_26_energy_shift(), activation=Activations.ONCE_PER_TURN), Attack(title='Ion Blast', game_text='You may do 40 damage plus 60 more damage. If you do, Electrode does 100 damage to itself.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=40, damage_operator='+', effect=dp3_electrode_26_ion_blast())])
