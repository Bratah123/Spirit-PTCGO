from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e59906b-1404-5891-b88d-83b56518a89c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=701,
    abilities=[
        Attack(
            title="Windfall",
            game_text="Shuffle your hand into your deck. Then, draw 5 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)