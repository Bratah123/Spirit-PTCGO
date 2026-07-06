from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0797b843-dbbd-512b-9582-2f55389fb9cb",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Fusion Strike", "Latios"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=194,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=381,
    abilities=[
        Ability(
            title="Blue Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latias.",
            effect=unimplemented,
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)