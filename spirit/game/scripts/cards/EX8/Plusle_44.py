"""STUB: effect not implemented — do not guess mechanics.
Plusle (EX8 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_basic_n, spark_vs_powers


card = PokemonCardDef(
    guid="3f45b4a6-628d-589d-bb14-84c1559efd4d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=311,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=call_for_family_basic_n(2),
        ),
        Attack(
            title="Positive Spark",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon that has any Pok\u00e9-Powers. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=spark_vs_powers(),
        ),
    ],
)