from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_item_card


async def spacing_out(ctx):
    """Flip a coin. If heads, heal 10 damage from this Pokémon."""
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if heads:
        await ctx.heal(10, ctx.attacker)


def _is_psychic_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


async def _scavenge(ctx):
    """Discard a Psychic Energy attached to this Pokemon. If you do, put an Item
    card from your discard pile into your hand."""
    if not any(_is_psychic_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        return
    gone = await ctx.discard_energy_from(ctx.attacker, 1, predicate=_is_psychic_energy, minimum=1)
    pool = [c for c in ctx.discard_pile() if is_item_card(c)]
    if gone and pool:
        pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Item card")
        await ctx.put_in_hand(pick)


card = PokemonCardDef(
    guid="39c432ae-497f-5878-a493-bffedc5920b2",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Spacing Out",
            game_text="Flip a coin. If heads, heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spacing_out,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard a Psychic Energy attached to this Pok\u00e9mon. If you do, put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=_scavenge,
        ),
    ],
)