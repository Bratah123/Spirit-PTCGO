from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def energy_wheel(ctx):
    """Move an Energy from 1 of your Benched Pokémon to this Pokémon."""
    bench = ctx.my_bench()
    if not bench or ctx.attacker is None:
        return
    await ctx.move_energy_freely(
        bench, [ctx.attacker],
        max_count=1,
        prompt="Choose an Energy to move to this Pokémon",
    )


async def hurricane(ctx):
    """80 damage. Move a basic Energy from this Pokémon to 1 Bench."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or ctx.attacker is None:
        return
    await ctx.move_energy_freely(
        [ctx.attacker], bench,
        predicate=is_basic_energy_card,
        max_count=1,
        prompt="Choose a basic Energy to move to the Bench",
    )


card = PokemonCardDef(
    guid="51c8de8a-a1e6-5ddb-96da-8d3f8c29329c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic", "Tornadus"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title="Energy Wheel",
            game_text="Move an Energy from 1 of your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_wheel,
        ),
        Attack(
            title="Hurricane",
            game_text="Move a basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=hurricane,
        ),
    ],
)
