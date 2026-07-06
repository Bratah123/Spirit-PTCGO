from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a175066a-4e1b-5f72-9144-dea4a170053d",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Ability(
            title="Lucky Match",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may flip a coin. If heads, put a Supporter card from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)