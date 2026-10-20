from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_psychic(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


async def _cosmic_circle(ctx):
    """100; move as many Psychic Energy among your Pokemon as you like."""
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    sources = [p for p in mine if any(_is_psychic(e) for e in ctx.attached_energies(p))]
    if sources and len(mine) > 1 and await ctx.ask_yes_no("Move Psychic Energy between your Pokémon?"):
        await ctx.move_energy_freely(sources, mine, predicate=_is_psychic)


card = PokemonCardDef(
    guid="3cd637f2-1e79-5c0c-8a22-54d6c7e4b1c7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeheeyemBREAK.Name",
    display_name="Beheeyem BREAK",
    searchable_by=["Beheeyem BREAK", "BREAK", "BeheeyemBREAK"],
    subtypes=["BREAK"],
    collector_number=135,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    family_id=606,
    abilities=[
        Attack(
            title="Cosmic Circle",
            game_text="Move as many Psychic Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=_cosmic_circle,
        ),
    ],
)