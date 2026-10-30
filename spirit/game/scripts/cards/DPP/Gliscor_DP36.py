"""STUB: effect not implemented — do not guess mechanics.
Gliscor (DPP #DP36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="8325a48b-1861-5453-99f8-3325922e0454",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=472,
    abilities=[
        Ability(
            title="Bind Eye",
            game_text="As long as Gliscor is your Active Pok\u00e9mon, your opponent can't remove any Special Conditions by evolving or devolving his or her Pok\u00e9mon. (This also includes putting a Pok\u00e9mon Level-Up card onto that Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Turn",
            game_text="Flip a coin. If heads, put damage counters on the Defending Pok\u00e9mon until it is 10HP away from being Knocked Out. If you do, shuffle Gliscor and all cards attached to it back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Friction Heat",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)