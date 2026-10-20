from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def magical_echo(ctx):
    """Move all damage counters from 1 of your Benched Pokemon to the opponent's Active."""
    damaged = [p for p in ctx.my_bench()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged or ctx.defender is None:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose a Benched Pokémon to move all damage counters from")
    if source is None:
        return
    await ctx.move_damage_counters(source, ctx.defender)


card = PokemonCardDef(
    guid="4c0b9f79-73e1-58a5-b2bc-efb86ffad3a3",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Windy Mischief",
            game_text="Move all damage counters from 1 of your Benched Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=magical_echo,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)