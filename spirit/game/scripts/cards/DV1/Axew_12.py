from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb34c9f5-938a-5ca7-87d6-416e8b969318",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=610,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Flip a coin. If heads, search your deck for Fraxure, reveal it, and put it into your hand, Shuffle your deck afterward.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)