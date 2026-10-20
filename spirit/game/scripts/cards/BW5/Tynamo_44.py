from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="49e9f325-fd73-5c8a-8de6-f32ae43b9277",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)