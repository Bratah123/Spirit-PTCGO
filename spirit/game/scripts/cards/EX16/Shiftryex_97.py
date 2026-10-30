"""STUB: effect not implemented — do not guess mechanics.
Shiftry ex (EX16 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import dirge_same_name, skill_hack_play_from_opp_hand
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce397bca-fa8f-58d5-8667-d30937f8affa",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftryex.Name",
    display_name="Shiftry ex",
    searchable_by=["Shiftry ex", "Stage 2", "ex", "Shiftryex"],
    subtypes=["Stage 2", "ex"],
    collector_number=97,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Skill Hack",
            game_text="Look at your opponent's hand and choose a Basic Pok\u00e9mon or Evolution card you find there. Choose 1 of that Pok\u00e9mon's attacks. Skill Hack copies that attack except for its Energy cost. (You must still do anything else required for that attack.) (No matter what type that Pok\u00e9mon is, Shiftry ex's type is still Darkness.) Shiftry ex performs that attack.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=skill_hack_play_from_opp_hand(),
        ),
        Attack(
            title="Dirge",
            game_text="Does 60 damage to each of your opponent's Benched Pok\u00e9mon that has the same name as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=dirge_same_name(60),
        ),
    ],
)