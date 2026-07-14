from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import is_supporter_card


def _no_supporter_in_discard(ctx) -> bool:
    return not any(is_supporter_card(c) for c in ctx.discard_pile())


card = PokemonCardDef(
    guid="90334fc1-7871-5630-8b70-5661f2027844",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Mystery Press",
            game_text="If you have no Supporter cards in your discard pile, this attack does 130 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_no_supporter_in_discard, 130),
        ),
    ],
)