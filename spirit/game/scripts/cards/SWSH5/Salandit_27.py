from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2fd8338-04ba-5d9b-b287-13edb65beede",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic", "Salandit"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Call Sign",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
    ],
)