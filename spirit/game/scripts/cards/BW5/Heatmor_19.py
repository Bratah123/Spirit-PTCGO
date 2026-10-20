from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="189e4828-817d-567f-a185-5f1d469e6359",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Hot Lick",
            game_text="If the Defending Pok\u00e9mon is Durant, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)