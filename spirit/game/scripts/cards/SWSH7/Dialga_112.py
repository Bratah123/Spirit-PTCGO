from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08afc319-a853-519a-a76d-c623406d483a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Single Strike", "Dialga"],
    subtypes=["Basic", "Single Strike"],
    collector_number=112,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=483,
    abilities=[
        Attack(
            title="Chrono Wind",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon V, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
        ),
    ],
)