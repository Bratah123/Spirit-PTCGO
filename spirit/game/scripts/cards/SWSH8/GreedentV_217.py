from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb93220a-360b-5958-b908-c7cd6eb5055b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentV.Name",
    display_name="Greedent V",
    searchable_by=["Greedent V", "Basic", "V", "GreedentV"],
    subtypes=["Basic", "V"],
    collector_number=217,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=820,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Nom-Nom-Nom Incisors",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)