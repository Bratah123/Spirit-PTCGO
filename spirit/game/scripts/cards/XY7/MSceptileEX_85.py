from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


async def _jagged_saber(ctx):
    """100; you may attach up to 2 Grass Energy from your hand to your Benched
    Pokemon in any way; heal all damage from each Pokemon that got Energy."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.hand() if _is_grass_energy(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Grass Energy") or []
    healed = []
    for energy in picks:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Attach to which Benched Pokémon?")
        if target is not None and await ctx.attach_energy(energy, target):
            if target not in healed:
                healed.append(target)
    for p in healed:
        dmg = ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)
        if dmg > 0:
            await ctx.heal(dmg, p)


card = PokemonCardDef(
    guid="a0eef803-61f5-574f-9f4e-e25d2f65853f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSceptileEX.Name",
    display_name="M Sceptile-EX",
    searchable_by=["M Sceptile-EX", "MEGA", "EX", "MSceptileEX"],
    subtypes=["MEGA", "EX"],
    collector_number=85,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    family_id=254,
    abilities=[
        ancient_trait('θ Stop'),
        Attack(
            title="Jagged Saber",
            game_text="You may attach up to 2 Grass Energy cards from your hand to your Benched Pok\u00e9mon in any way you like. If you attached Energy to a Pok\u00e9mon in this way, heal all damage from that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_jagged_saber,
        ),
    ],
)