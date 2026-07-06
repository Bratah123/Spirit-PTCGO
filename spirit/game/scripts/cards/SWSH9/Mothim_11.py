from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="036eec95-ef8e-555c-94e4-492ddbef4175",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name",
    display_name="Mothim",
    searchable_by=["Mothim", "Stage 1", "Mothim"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Raid",
            game_text="If this Pok\u00e9mon evolved from Burmy during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)