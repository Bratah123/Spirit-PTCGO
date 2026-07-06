from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2137a21d-8c55-54ef-a688-dc8748e37904",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic", "Zamazenta"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=889,
    abilities=[
        Attack(
            title="Metal Armament",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Amazing Shield",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)