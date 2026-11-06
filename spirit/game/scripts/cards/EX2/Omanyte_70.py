from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import search_to_bench_named


card = PokemonCardDef(
    guid="c45aed7a-2dc6-55c9-8b0f-b8c06b64abf3",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Team Assembly",
            game_text="Search your deck for Omanyte, Kabuto, or any Basic Pok\u00e9mon and put as many of them as you like onto your Bench. Shuffle your deck afterward. Treat the new Benched Pok\u00e9mon as Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench_named(
                "Omanyte", "Kabuto", include_basic=True,
                prompt="Choose Omanyte, Kabuto, or Basic Pokémon to put onto your Bench.",
            ),
        ),
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
