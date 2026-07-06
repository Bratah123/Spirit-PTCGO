from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ede15548-4198-553f-b086-db639fbd0c08",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)