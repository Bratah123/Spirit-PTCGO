from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="80c1d2ca-0559-5d32-962e-8679c9c7d324",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    display_name="Gossifleur",
    searchable_by=["Gossifleur", "Basic", "Gossifleur"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=829,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)