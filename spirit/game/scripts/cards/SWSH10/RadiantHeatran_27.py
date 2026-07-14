from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on

card = PokemonCardDef(
    guid="32d3df0a-a32e-59fd-9b9c-5df50971c393",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantHeatran.Name",
    display_name="Radiant Heatran",
    searchable_by=["Radiant Heatran", "Basic", "Radiant", "RadiantHeatran"],
    subtypes=["Basic", "Radiant"],
    collector_number=27,
    set_code="SWSH10",
    rarity=Rarities.RareRadiant,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Raging Blast",
            game_text="This attack does 70 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 70),
        ),
    ],
)