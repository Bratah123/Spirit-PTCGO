from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a04f7682-a3ef-5a49-bd8a-ecd2452a0fde",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)