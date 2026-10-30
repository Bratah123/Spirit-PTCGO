from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import flip_bonus


def _is_stadium(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


async def _land_maker(ctx):
    """Put 2 Stadium cards from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if _is_stadium(c)]
    n = min(2, len(pool))
    if not n:
        return
    picks = pool if len(pool) == n else await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Stadium cards")
    if picks:
        await ctx.put_in_hand(list(picks))


card = PokemonCardDef(
    guid="fcbe0349-a94b-595d-adb4-effe08a8352a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Land Maker",
            game_text="Put 2 Stadium cards from your discard pile into your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=_land_maker,
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)