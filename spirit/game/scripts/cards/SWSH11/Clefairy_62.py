from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77c480af-bb9a-5b71-b32f-41a2c325236e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=35,
    abilities=[
        Ability(
            title="Moon-Watching Party",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, for each of your Benched Clefairy, you may search your deck for a Psychic Energy card and attach it to that Clefairy. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Wonder Storm",
            game_text="This attack does 20 damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)