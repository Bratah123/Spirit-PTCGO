from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import search_to_bench_named
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="b03b1222-6767-5762-85de-6292287e0517",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Kabuto by attacks is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=takes_less_passive(20),
        ),
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
            title="Pierce",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
