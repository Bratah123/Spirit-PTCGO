from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="5456f342-bf29-5669-9dbe-463ed235f594",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title="Entrainment",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2, prompt='Choose up to 2 Basic Pokémon to put onto your Bench.'),
        ),
        Attack(
            title="Energy Short",
            game_text="This attack does 20 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy('defender'), 20),
        ),
    ],
)