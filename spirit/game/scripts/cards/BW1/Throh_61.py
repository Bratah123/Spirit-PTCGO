from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af79d6bc-e4c6-5c56-8ce3-41f781f5f899",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic", "Throh"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Circle Throw",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Storm Throw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)