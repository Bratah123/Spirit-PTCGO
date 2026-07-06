from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e2205d31-0aff-56a6-a859-8649abc57a10",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantV.Name",
    display_name="Hisuian Lilligant V",
    searchable_by=["Hisuian Lilligant V", "Basic", "V", "HisuianLilligantV"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=549,
    abilities=[
        Attack(
            title="Dance Gracefully",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)