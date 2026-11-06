from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import rock_tumble


card = PokemonCardDef(
    guid="eba559ac-1002-5fbd-8cfa-19c001bb3f64",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    display_name="Geodude",
    searchable_by=["Geodude", "Basic", "Geodude"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=74,
    abilities=[
        Attack(
            title="Rock Hurl",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=rock_tumble,
        ),
    ],
)
