from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a01ecb8-7a8e-5fcc-8a14-9e7a5f8f50c4",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=216,
    abilities=[
        Attack(
            title="Baby-Doll Eyes",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
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