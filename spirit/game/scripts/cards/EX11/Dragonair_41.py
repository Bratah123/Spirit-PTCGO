"""STUB: effect not implemented — do not guess mechanics.
Dragonair δ (EX11 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import slam_flip
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="571b6e67-a589-5b81-a12e-1673c68179c5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair δ",
    searchable_by=["Dragonair \u03b4", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=148,
    abilities=[
        Attack(
            title="Slam",
            game_text="Flip 2 coin. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=slam_flip(20, 2),
        ),
        Attack(
            title="Dragon Rage",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)