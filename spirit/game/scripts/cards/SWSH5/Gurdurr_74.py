from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="80437d3d-21d2-519c-9415-8a61ac4373a3",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1", "Gurdurr"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)