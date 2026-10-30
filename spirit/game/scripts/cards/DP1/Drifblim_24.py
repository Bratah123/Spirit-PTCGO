"""STUB: effect not implemented — do not guess mechanics.
Drifblim (DP1 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.dp import wind_wave_recover


card = PokemonCardDef(
    guid="7b9c3b95-a33f-5d5a-ac3f-abd839dfd34f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
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
            title="Wind Wave",
            game_text="Search your discard pile for up to 5 in any combination of Pok\u00e9mon and Supporter cards. Show them to your opponent and shuffle them into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wind_wave_recover(5),
        ),
        Attack(
            title="Explosive Smoke",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            effect=spread_damage(10, side='both', also_base=True),
        ),
    ],
)