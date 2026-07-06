from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c37cbc6-f755-5bf8-b252-55099c40509a",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name",
    display_name="Galarian Ponyta",
    searchable_by=["Galarian Ponyta", "Basic", "GalarianPonyta"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=77,
    abilities=[
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)