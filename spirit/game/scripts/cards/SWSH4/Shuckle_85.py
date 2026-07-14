from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def deck_distiller(ctx):
    heads = await ctx.flip_until_tails("Deck Distiller")
    if heads <= 0:
        return
    top_cards = ctx.deck_top(heads, ctx.opponent_id)
    if top_cards:
        await ctx.discard_cards(top_cards)

card = PokemonCardDef(
    guid="227f3371-a80d-5801-9dd9-7fce3191efe5",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=213,
    abilities=[
        Attack(
            title="Deck Distiller",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=deck_distiller,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)