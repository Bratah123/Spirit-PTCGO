from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d799e888-b9fa-5bb8-b022-acc672128675",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantEternatus.Name",
    display_name="Radiant Eternatus",
    searchable_by=["Radiant Eternatus", "Basic", "Radiant", "RadiantEternatus"],
    subtypes=["Basic", "Radiant"],
    collector_number=105,
    set_code="CZ",
    rarity=Rarities.RareRadiant,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=890,
    abilities=[
        Ability(
            title="Climactic Gate",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 2 Pok\u00e9mon VMAX and put them onto your Bench. Then, shuffle your deck. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
        ),
    ],
)