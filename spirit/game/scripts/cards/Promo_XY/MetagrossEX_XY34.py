from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_metal(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


async def _magnetic_laser(ctx):
    """20; you may move a Metal Energy from 1 of your Benched Pokemon to this Pokemon."""
    await ctx.deal_damage()
    sources = [p for p in ctx.my_bench() if any(_is_metal(e) for e in ctx.attached_energies(p))]
    if sources and await ctx.ask_yes_no("Move a Metal Energy from your Bench to this Pokémon?"):
        await ctx.move_energy_freely(sources, [ctx.attacker], predicate=_is_metal, max_count=1)


card = PokemonCardDef(
    guid="0b36186e-dd0c-5fe5-839e-9dcc6f5ed0ba",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossEX.Name",
    display_name="Metagross-EX",
    searchable_by=["Metagross-EX", "Basic", "EX", "MetagrossEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=376,
    abilities=[
        Attack(
            title="Magnetic Laser",
            game_text="You may move a Metal Energy from 1 of your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_magnetic_laser,
        ),
        Attack(
            title="Squared Attack",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)