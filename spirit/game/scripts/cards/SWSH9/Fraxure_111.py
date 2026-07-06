from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d9aa35c-bfbc-50c0-94b3-7ae26b7a84f6",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1", "Fraxure"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=60,
        ),
    ],
)