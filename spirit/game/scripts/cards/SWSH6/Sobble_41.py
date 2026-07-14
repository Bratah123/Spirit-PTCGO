from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon


def _is_basic_rapid_strike(card):
    return is_basic_pokemon(card) and "Rapid Strike" in subtypes_for(card.archetype_id)

card = PokemonCardDef(
    guid="585cecee-cbc1-55ee-96f6-3f797cb366a6",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    display_name="Sobble",
    searchable_by=["Sobble", "Basic", "Rapid Strike", "Sobble"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=41,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Keep Calling",
            game_text="Search your deck for up to 3 Basic Rapid Strike Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(predicate=_is_basic_rapid_strike, count=3),
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)