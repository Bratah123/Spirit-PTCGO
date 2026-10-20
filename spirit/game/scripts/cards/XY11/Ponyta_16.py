from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _returning_flames(ctx):
    """Put 2 Fire Energy cards from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if pool:
        n = min(2, len(pool))
        picked = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Fire Energy cards")
        await ctx.put_in_hand(picked)


card = PokemonCardDef(
    guid="c2a07789-8bf2-5c80-a72a-0d877c99ddec",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Returning Flames",
            game_text="Put 2 Fire Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_returning_flames,
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)