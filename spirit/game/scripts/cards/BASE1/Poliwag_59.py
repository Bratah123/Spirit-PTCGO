from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import unused_energy_bonus


card = PokemonCardDef(
    guid="49d22aab-f2f0-5c93-8e8a-f843ed0d1794",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic", "Poliwag"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="BASE1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Poliwag but not used to pay for this attack's Energy cost. Extra Water Energy after the 2nd don't count.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20, energy_type=PokemonTypes.WATER),
        ),
    ],
)
