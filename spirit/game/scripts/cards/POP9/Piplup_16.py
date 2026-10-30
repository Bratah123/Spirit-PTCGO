"""Piplup (POP9 #16)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import less_energy_bonus, partner_bench_spread


card = PokemonCardDef(
    guid="27395021-3304-5e2f-8822-46be3e0e2c56",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic", "Piplup"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Water Sport",
            game_text="If Piplup has less Energy attached to it than the Defending Pok\u00e9mon, this attack does 10 damage plus more 10 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=less_energy_bonus(10)
        ),
        Attack(
            title="Wavelet",
            game_text="If you have Buizel in play, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=partner_bench_spread('Buizel', 10)
        ),
    ]
)