from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _named(p, *names):
    return getattr(def_for(p.archetype_id), "display_name", None) in names


async def _eon_connection(ctx):
    """Draw a card; draw 1 more if Latios is on your Bench."""
    extra = 1 if any(_named(p, "Latios") for p in ctx.my_bench()) else 0
    await ctx.draw_cards(1 + extra)


card = PokemonCardDef(
    guid="a31574f9-a434-5ce2-9a41-871afc9fd502",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=380,
    abilities=[
        Attack(
            title="Eon Connection",
            game_text="Draw a card. If Latios is on your Bench, draw 1 more card.",
            cost={PokemonTypes.FIRE: 1},
            effect=_eon_connection,
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)