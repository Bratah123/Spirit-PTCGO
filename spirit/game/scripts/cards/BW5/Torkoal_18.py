from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _flame_cloak(ctx):
    """Printed damage; flip, heads attach a Fire Energy card from your discard
    pile to this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Flame Cloak")
    if not results or not results[0]:
        return
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Fire Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="edbe0ea0-1406-52dc-97c7-d035128e328a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Flip a coin. If heads, attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_flame_cloak,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)