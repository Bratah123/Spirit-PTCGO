from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78588e27-cef4-52b1-b04d-2c3474ffb2a7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissVMAX.Name",
    display_name="Togekiss VMAX",
    searchable_by=["Togekiss VMAX", "VMAX", "TogekissVMAX"],
    subtypes=["VMAX"],
    collector_number=141,
    set_code="SWSH4",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissV.Name",
    family_id=468,
    abilities=[
        Attack(
            title="Max Glide",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)