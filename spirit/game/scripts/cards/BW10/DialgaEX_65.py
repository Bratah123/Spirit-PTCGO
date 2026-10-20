from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
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
    guid="7e21be66-22d5-5f76-a4f6-f398976750fb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaEX.Name",
    display_name="Dialga-EX",
    searchable_by=["Dialga-EX", "Basic", "EX", "Team Plasma", "DialgaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=65,
    set_code="BW10",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    family_id=483,
    abilities=[
        Attack(
            title="Reverse Edge",
            game_text="Flip a coin. If heads, put a card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_or_nothing(then=_put_discard_card_in_hand),
        ),
        Attack(
            title="Fast Forward",
            game_text="For each Plasma Energy attached to this Pok\u00e9mon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            effect=unimplemented,
        ),
    ],
)