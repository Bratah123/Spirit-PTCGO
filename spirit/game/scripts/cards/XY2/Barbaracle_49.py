"""STUB: effect not implemented — do not guess mechanics.
Barbaracle (XY2 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="374729a7-d56c-580f-9f5d-38daf420f121",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Attack(
            title="Rock Rush",
            game_text="Discard as many Fighting Energy cards as you like from your hand. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
        ),
    ],
)