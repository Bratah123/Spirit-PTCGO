from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _draw_in(ctx):
    """Attach 2 Fire Energy cards from your discard pile to this Pokemon."""
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if not pool:
        return
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Fire Energy cards to attach")
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="a64bc044-ae1a-54e4-b745-12b1fbb71486",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Draw In",
            game_text="Attach 2 Fire Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=_draw_in,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)