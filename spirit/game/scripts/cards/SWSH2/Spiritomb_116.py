from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0199bea8-9023-57e2-b9f0-3c6e303d8dac",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Splitting Spite",
            game_text="Discard the top card of each player's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dripping Grudge",
            game_text="Put 1 damage counter on your opponent's Active Pok\u00e9mon for each Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)