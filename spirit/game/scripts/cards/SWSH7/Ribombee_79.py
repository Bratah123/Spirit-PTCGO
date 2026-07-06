from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84012bef-c137-55bc-a645-f9eade5ee78d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1", "Ribombee"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Attack(
            title="Tricky Steps",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)