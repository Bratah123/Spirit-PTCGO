from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="2c9fe9a1-480b-5cc6-9baf-f31459f9173e",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=605,
    abilities=[
        Attack(
            title="First Contact",
            game_text="Search your deck for 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
