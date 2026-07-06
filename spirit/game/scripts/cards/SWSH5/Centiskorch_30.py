from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f61cb59b-d8ab-5de7-924e-ea9da902a205",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1", "Centiskorch"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Ability(
            title="Overheater",
            game_text="Whenever your opponent flips a coin for their Burned Pok\u00e9mon during Pok\u00e9mon Checkup, it doesn't recover from that Special Condition even if the result is heads.",
            effect=unimplemented,
        ),
        Attack(
            title="Bursting Inferno",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)