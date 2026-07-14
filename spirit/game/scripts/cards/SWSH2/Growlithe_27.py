from spirit.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="32995129-62da-5065-b2c7-ca1ae5bb1e1b",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip a coin. If heads, put a card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=_put_discard_card_in_hand),
        ),
        Attack(
            title="Fire Claws",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)