from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="026d6885-9216-5891-83ce-9a93c8672e0f",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=150,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Big Throw",
            game_text="Flip a coin. If heads, discard your opponent's Active Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=unimplemented,
        ),
    ],
)