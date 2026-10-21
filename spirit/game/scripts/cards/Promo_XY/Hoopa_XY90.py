from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.content.definitions import def_for


def _named(p, *names):
    return getattr(def_for(p.archetype_id), "display_name", None) in names


async def _summoning_draw(ctx):
    """If Pikachu is on your Bench, draw 3 cards."""
    if any(_named(p, "Pikachu") for p in ctx.my_bench()):
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="83338d69-3f72-59c7-9403-0f795cea3be9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Summoning Draw",
            game_text="If Pikachu is on your Bench, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_summoning_draw,
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)