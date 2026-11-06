from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import call_for_family_condition, named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="664ba19e-344e-5c4a-b249-db82a980439c",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran \u2640", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon named Nidoran \u2642 or Nidoran \u2640 and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.GRASS: 2},
            condition=call_for_family_condition,
            effect=search_to_bench(
                predicate=named_basic("Nidoran"),
                prompt="Choose a Nidoran ♂ or Nidoran ♀ to put onto your Bench.",
            ),
        ),
    ],
)
