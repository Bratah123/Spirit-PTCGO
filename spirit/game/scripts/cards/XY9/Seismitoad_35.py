"""STUB: effect not implemented — do not guess mechanics.
Seismitoad (XY9 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae58c071-f371-5d56-8258-bcfa757d06b9",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Siphon Off",
            game_text="Attach 3 Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shaky Fall",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. That Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 4},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)