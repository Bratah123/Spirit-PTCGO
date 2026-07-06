from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a7dce38-afce-55cf-a1b4-23e337fab2ba",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic", "Sandile"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=551,
    abilities=[
        Attack(
            title="Dredge Up",
            game_text="Discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=unimplemented,
        ),
    ],
)