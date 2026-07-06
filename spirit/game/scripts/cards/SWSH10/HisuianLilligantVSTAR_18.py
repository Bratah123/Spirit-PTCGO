from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4816d51d-d3b7-5122-b7ce-93e30fbdbd30",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantVSTAR.Name",
    display_name="Hisuian Lilligant VSTAR",
    searchable_by=["Hisuian Lilligant VSTAR", "VSTAR", "HisuianLilligantVSTAR"],
    subtypes=["VSTAR"],
    collector_number=18,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantV.Name",
    family_id=549,
    abilities=[
        Ability(
            title="Star Perfume",
            game_text="During your turn, you may search your deck for up to 5 in any combination of Grass Pok\u00e9mon and Grass Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Parallel Spin",
            game_text="You may put an Energy attached to this Pok\u00e9mon into your hand. If you do, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)