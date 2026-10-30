"""STUB: effect not implemented — do not guess mechanics.
Tyranitar ex (POP1 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import critical_crush_discard_basic
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5be753e5-3531-503e-bfe0-577dbcbd237b",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex",
    searchable_by=["Tyranitar ex", "Stage 2", "ex", "Tyranitarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=17,
    set_code="POP1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Critical Crush",
            game_text="Discard 2 Basic Energy cards attached to Tyranitar ex or this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=critical_crush_discard_basic(2),
        ),
    ],
)