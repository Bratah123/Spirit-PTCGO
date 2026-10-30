"""STUB: effect not implemented — do not guess mechanics.
Kingdra ex δ (EX15 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import energy_link_attach_from_discard_to_self, extra_smoke_stage2_ex_reduce, protective_swirl_no_weakness_next
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="010574aa-3bc8-5151-a970-9605e9423c57",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdraex.Name",
    display_name="Kingdra ex δ",
    searchable_by=["Kingdra ex \u03b4", "Stage 2", "ex", "Kingdraex"],
    subtypes=["Stage 2", "ex"],
    collector_number=94,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Ability(
            title="Extra Smoke",
            game_text="Any damage done to your Stage 2 Pok\u00e9mon-ex by your opponent's attacks is reduced by 10 (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=extra_smoke_stage2_ex_reduce(10),
        ),
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Kingdra ex.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=energy_link_attach_from_discard_to_self(),
        ),
        Attack(
            title="Protective Swirl",
            game_text="Kingdra ex has no Weakness during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=protective_swirl_no_weakness_next(),
        ),
    ],
)