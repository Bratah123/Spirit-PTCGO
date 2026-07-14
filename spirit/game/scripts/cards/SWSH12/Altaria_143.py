from spirit.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="f2d2baea-17a0-5dc7-b6aa-bbe37feca0ec",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=143,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Magical Echo",
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=magical_echo,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
