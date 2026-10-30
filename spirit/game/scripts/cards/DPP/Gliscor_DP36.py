"""STUB: effect not implemented — do not guess mechanics.
Gliscor (DPP #DP36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    dpp_gliscor_dp36_bind_eye_passive,
    dpp_gliscor_dp36_cutting_turn,
)

card = PokemonCardDef(guid='8325a48b-1861-5453-99f8-3325922e0454', key='DPP', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name', display_name='Gliscor', searchable_by=['Gliscor', 'Stage 1', 'Gliscor'], subtypes=['Stage 1'], collector_number=36, set_code='DPP', rarity=Rarities.RarePromo, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name', family_id=472, abilities=[Ability(title='Bind Eye', game_text="As long as Gliscor is your Active Pokémon, your opponent can't remove any Special Conditions by evolving or devolving his or her Pokémon. (This also includes putting a Pokémon Level-Up card onto that Pokémon.)", ability_type=AbilityTypes.POKE_BODY, passive=dpp_gliscor_dp36_bind_eye_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Cutting Turn', game_text='Flip a coin. If heads, put damage counters on the Defending Pokémon until it is 10HP away from being Knocked Out. If you do, shuffle Gliscor and all cards attached to it back into your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=dpp_gliscor_dp36_cutting_turn()), Attack(title='Friction Heat', game_text='The Defending Pokémon is now Burned.', cost={PokemonTypes.FIGHTING: 1}, damage=20, effect=condition_attack(SpecialConditions.BURNED))])
