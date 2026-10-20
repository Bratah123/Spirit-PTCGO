from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import damage_per, count_bench


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _burning_roar(ctx):
    """Discard the top 4 cards of your deck; attach any Fire Energy among them
    to your Pokemon in any way."""
    top = ctx.deck_top(4)
    if not top:
        return
    await ctx.discard_cards(top)
    for energy in [c for c in top if _is_fire_energy(c)]:
        mine = ctx.my_pokemon_in_play()
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach the Fire Energy to which Pokémon?")
        if target is not None:
            await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="6decb528-a0f3-5fdf-8d6a-d44b9e8ca759",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Burning Roar",
            game_text="Discard the top 4 cards of your deck. If any of those cards are Fire Energy cards, attach them to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_burning_roar,
        ),
        Attack(
            title="Combat Blaze",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench('opponent'), 20, base=20),
        ),
    ],
)