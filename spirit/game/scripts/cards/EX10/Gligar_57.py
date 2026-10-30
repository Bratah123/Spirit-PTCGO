"""STUB: effect not implemented — do not guess mechanics.
Gligar (EX10 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import free_flight_no_energy_passive


card = PokemonCardDef(
    guid="26b359f1-96bb-5504-990e-4c0bf59960da",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=207,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If Gligar has no Energy cards attached to it, Gligar's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=free_flight_no_energy_passive(),
        ),
        Attack(
            title="Toxic Grip",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)