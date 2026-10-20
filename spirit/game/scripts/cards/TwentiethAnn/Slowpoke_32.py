"""STUB: effect not implemented — do not guess mechanics.
Slowpoke (TwentiethAnn #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def spacing_out(ctx):
    """Flip a coin. If heads, heal 10 damage from this Pokémon."""
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if heads:
        await ctx.heal(10, ctx.attacker)


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
            # STUB: attack effect not implemented
            effect=spacing_out,
        ),
        Attack(
            title="Scavenge",
            game_text="Discard a Psychic Energy attached to this Pok\u00e9mon. If you do, put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)