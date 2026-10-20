from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_retreat_cost


async def _thorn_tempest(ctx):
    """When played from hand to evolve: you may put 1 damage counter on each
    of your opponent's Pokemon."""
    if not await ctx.ask_yes_no("Put 1 damage counter on each of your opponent's Pokémon?"):
        return
    for p in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=p, apply_modifiers=False, is_attack=False,
                              as_counters=True)


async def _iron_crash(ctx):
    """20 more damage for each Colorless in the opponent's Active's Retreat Cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage(20 + 20 * cost)


card = PokemonCardDef(
    guid="b397933b-333b-5f98-b58f-57e7610732cd",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Thorn Tempest",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_thorn_tempest,
        ),
        Attack(
            title="Iron Crash",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=_iron_crash,
        ),
    ],
)