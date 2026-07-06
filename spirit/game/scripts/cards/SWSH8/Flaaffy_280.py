from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08c40df4-a437-5bf4-95a8-f5b2b5f4719f",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=280,
    set_code="SWSH8",
    rarity=Rarities.RareSecret,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=180,
    abilities=[
        Ability(
            title="Dynamotor",
            game_text="Once during your turn (before your attack), you may attach a Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)