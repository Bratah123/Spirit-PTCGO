"""STUB: effect not implemented — do not guess mechanics.
Luxray (XY9 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="25d00913-a8ce-5666-a281-1c85d292e7e5",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Snarl",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)