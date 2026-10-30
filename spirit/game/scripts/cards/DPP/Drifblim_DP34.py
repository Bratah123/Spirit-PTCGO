"""STUB: effect not implemented — do not guess mechanics.
Drifblim (DPP #DP34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ebcb89b-fb22-59f2-8a17-480f6a3738cc",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=426,
    abilities=[
        Attack(
            title="Wind Wave",
            game_text="Search your discard pile for up to 5 in any combination of Pok\u00e9mon and Supporter cards. Show them to your opponent and shuffle them into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Explosive Smoke",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)