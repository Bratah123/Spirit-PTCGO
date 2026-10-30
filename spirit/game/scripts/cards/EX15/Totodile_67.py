"""STUB: effect not implemented — do not guess mechanics.
Totodile δ (EX15 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import rage_damage
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="261472c0-8cb3-5455-9544-34566205047d",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile δ",
    searchable_by=["Totodile \u03b4", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=158,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Totodile.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=rage_damage(10, 10),
        ),
    ],
)