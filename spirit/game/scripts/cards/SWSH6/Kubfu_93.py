from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e752614-cfb1-5199-bc31-20cc4833fb06",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kubfu.Name",
    display_name="Kubfu",
    searchable_by=["Kubfu", "Basic", "Kubfu"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=891,
    abilities=[
        Attack(
            title="Training",
            game_text="Search your deck for a basic Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Elbow Strike",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)