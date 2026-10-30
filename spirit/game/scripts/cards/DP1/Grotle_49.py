"""STUB: effect not implemented — do not guess mechanics.
Grotle (DP1 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import synthesis_attach

card = PokemonCardDef(
    guid="b7cbd44f-383b-57e3-99b6-273ed31900e5",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    display_name="Grotle",
    searchable_by=["Grotle", "Stage 1", "Grotle"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=synthesis_attach(),
        ),
        Attack(
            title="Cut",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)