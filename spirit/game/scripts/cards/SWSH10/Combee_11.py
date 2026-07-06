from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a8d10f5-1245-56ad-bb4e-a603d075f710",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic", "Combee"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=415,
    abilities=[
        Attack(
            title="Honey Courier",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)