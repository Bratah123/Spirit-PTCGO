from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def joust(ctx):
    defender = ctx.opponent_active()
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [tool for tool, pokemon in ctx.tools_in_play() if pokemon is defender]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


async def reflect_energy(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if energies and bench:
        picked = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to move")
        if picked:
            target = await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to move the Energy to"
            )
            if target is not None:
                await ctx.move_energy(picked[0], target)


card = PokemonCardDef(
    guid="b942edb8-af0e-58a1-b735-fd6f3a2e8361",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=561,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=joust,
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=reflect_energy,
        ),
    ],
)