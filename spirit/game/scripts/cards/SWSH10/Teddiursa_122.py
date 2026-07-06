from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a219f96-c79a-5587-a827-38583c333b0f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=216,
    abilities=[
        Attack(
            title="Gather Food",
            game_text="Flip a coin. If heads, put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)