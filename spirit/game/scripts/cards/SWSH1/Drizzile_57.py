from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7f9fa5a-db4e-5b47-a1b9-c247d64f3e6b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    display_name="Drizzile",
    searchable_by=["Drizzile", "Stage 1", "Drizzile"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)