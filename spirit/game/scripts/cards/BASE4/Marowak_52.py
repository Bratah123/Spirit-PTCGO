from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import basic_of_type, call_for_family_condition
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="e8767f56-994d-5514-8357-2f4ce442dbb4",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Bonemerang",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Call for Friend",
            game_text="Search your deck for a Fighting Basic Pok\u00e9mon card and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            condition=call_for_family_condition,
            effect=search_to_bench(
                predicate=basic_of_type(PokemonTypes.FIGHTING),
                prompt="Choose a Fighting Basic Pokémon to put onto your Bench.",
            ),
        ),
    ],
)
