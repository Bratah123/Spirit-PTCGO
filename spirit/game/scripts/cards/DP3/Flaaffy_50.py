"""STUB: effect not implemented — do not guess mechanics.
Flaaffy (DP3 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="576331dc-688a-5a48-96d9-d27dba837207",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Attract Current",
            game_text="Search your deck for a Lightning Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electromagnetic Kick",
            game_text="Flip a coin. If tails, Flaaffy does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)