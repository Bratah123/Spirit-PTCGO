"""STUB: effect not implemented — do not guess mechanics.
Muk ex (EX3 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import toxic_gas_passive, slimy_water


card = PokemonCardDef(
    guid="94b3e0ca-eb84-576d-87b6-465aaa54c51b",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mukex.Name",
    display_name="Muk ex",
    searchable_by=["Muk ex", "Stage 1", "ex", "Mukex"],
    subtypes=["Stage 1", "ex"],
    collector_number=96,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Toxic Gas",
            game_text="As long as Muk ex is your Active Pok\u00e9mon, ignore all Pok\u00e9-Powers and Pok\u00e9-Bodies other than Toxic Gas.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=toxic_gas_passive(),
        ),
        Attack(
            title="Poison Breath",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Slimy Water",
            game_text="Does 40 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=slimy_water(40, 10),
        ),
    ],
)