from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import unused_energy_bonus


card = PokemonCardDef(
    guid="508c96d2-1a3a-5896-a7c1-015ff7b764e7",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Water Gun",
            game_text="Does 30 damage plus 10 more damage for each Water Energy attached to Vaporeon but not used to pay for this attack's Energy cost. Extra Water Energy after the 2nd doesn't count.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20, energy_type=PokemonTypes.WATER),
        ),
    ],
)
