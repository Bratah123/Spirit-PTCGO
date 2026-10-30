"""STUB: effect not implemented — do not guess mechanics.
Drifblim (DP7 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c6739061-7c51-55b1-b200-c0dbf52def27",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Delivery",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lifting",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. For each Basic Pok\u00e9mon you put onto your Bench, you may search your deck for a basic Energy card and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ominous Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)