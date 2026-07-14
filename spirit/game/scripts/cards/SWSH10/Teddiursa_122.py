from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card


async def gather_food(ctx):
    """Flip a coin. If heads, put an Item card from your discard pile into your hand."""
    heads = await ctx.flip_coins(1, "Gather Food")
    if not heads[0]:
        return
    items = [c for c in ctx.discard_pile() if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(
        items, 1, minimum=0,
        prompt="Choose an Item card to put into your hand",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)

card = PokemonCardDef(
    guid="3a219f96-c79a-5587-a827-38583c333b0f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=216,
    abilities=[
        Attack(
            title="Gather Food",
            game_text="Flip a coin. If heads, put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gather_food,
        ),
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)