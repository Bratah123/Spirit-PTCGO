from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="a33e0208-4c25-5ecb-ab0f-760388d221d9",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic", "Emolga"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=587,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)