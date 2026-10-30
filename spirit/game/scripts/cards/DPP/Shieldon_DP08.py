"""STUB: effect not implemented — do not guess mechanics.
Shieldon (DPP #DP08): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8f692a25-6c27-51c9-8df2-fcbf969b1565",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    display_name="Shieldon",
    searchable_by=["Shieldon", "Stage 1", "Shieldon"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArmorFossil.Name",
    family_id=410,
    abilities=[
        Attack(
            title="Hard Face",
            game_text="During your opponent's next turn, any damage done to Shieldon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shield Attack",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)