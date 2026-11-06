from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _negative_discard(ctx):
    """Put 2 basic Energy cards from your discard pile into your hand."""
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 2, minimum=min(2, len(cards)),
                                   prompt="Choose 2 basic Energy cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="d7835845-1f24-5a5d-8c46-6375b8a20f08",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=312,
    abilities=[
        Attack(
            title="Negative Discard",
            game_text="Put 2 basic Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_negative_discard,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)