from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="080590a2-5fbf-57df-957a-1228e9c3fd6a",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Curtain",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Basic Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)