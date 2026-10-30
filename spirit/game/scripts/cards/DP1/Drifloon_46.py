"""STUB: effect not implemented — do not guess mechanics.
Drifloon (DP1 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import ominous_wind_confuse_lock
from spirit.game.card_effects.dp import blowing_wind_bench_to_deck


card = PokemonCardDef(
    guid="2e50270c-aff6-5ec2-b8f6-a3b5a2af515b",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Attack(
            title="Blowing Wind",
            game_text="Flip a coin. If heads, put 1 of your Benched Pok\u00e9mon and all cards attached to on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=blowing_wind_bench_to_deck(),
        ),
        Attack(
            title="Ominous Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ominous_wind_confuse_lock(10),
        ),
    ],
)