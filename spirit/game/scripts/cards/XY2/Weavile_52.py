from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="979ab486-17c7-5fbf-bbd0-368063dd0d2e",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2, prompt='Choose up to 2 Basic Pokémon to put onto your Bench.'),
        ),
        Attack(
            title="Claw Rend",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage(), 30),
        ),
    ],
)