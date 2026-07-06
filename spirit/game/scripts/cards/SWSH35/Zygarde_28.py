from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1822a90-07ef-5210-98b4-dcd5c77d1dff",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard a Fighting Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)