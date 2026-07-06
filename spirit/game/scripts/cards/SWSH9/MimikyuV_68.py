from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fa8ad8a-cb4a-5b13-84a4-5f71d12aa6e4",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuV.Name",
    display_name="Mimikyu V",
    searchable_by=["Mimikyu V", "Basic", "V", "MimikyuV"],
    subtypes=["Basic", "V"],
    collector_number=68,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=778,
    abilities=[
        Ability(
            title="Dummy Doll",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may prevent all damage done to this Mimikyu V by attacks from your opponent's Pok\u00e9mon until the end of your opponent's next turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Jealous Eyes",
            game_text="Put 3 damage counters on your opponent's Active Pok\u00e9mon for each Prize card your opponent has taken.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)