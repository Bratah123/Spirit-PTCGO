"""STUB: effect not implemented — do not guess mechanics.
Seadra δ (EX15 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import extra_ball_vs_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e93e6276-994b-5ff3-a55c-7b0296001077",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra δ",
    searchable_by=["Seadra \u03b4", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=117,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Extra Ball",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-ex, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_ball_vs_ex(30, 30),
        ),
    ],
)