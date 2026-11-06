from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def _put_discard_card_in_hand(ctx):
    discard = ctx.discard_pile()
    if not discard:
        return
    picks = await ctx.choose_cards(
        discard, 1, minimum=1,
        prompt="Choose a card from your discard pile to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="bb19e3a7-3bf2-5422-ba81-5abd8adb81c9",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic", "Woobat"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=527,
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip a coin. If heads, put a card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=_put_discard_card_in_hand),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)