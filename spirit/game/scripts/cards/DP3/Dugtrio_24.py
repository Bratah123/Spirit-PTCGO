"""STUB: effect not implemented — do not guess mechanics.
Dugtrio (DP3 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eaaface5-70d1-562d-ad8a-4b74c43a6833",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Dig Trap",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of an attack, including damage, done to Dugtrio during your opponent's next turn. If Dugtrio is your Active Pok\u00e9mon at the end of your opponent's next turn, put 6 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pit Trap",
            game_text="Your opponent flips a coin. If tails, this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)