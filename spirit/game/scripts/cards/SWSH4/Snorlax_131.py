from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a8d2e58-3006-5938-9f0e-5e3ff22b3185",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Gormandize",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw cards until you have 7 cards in your hand. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)