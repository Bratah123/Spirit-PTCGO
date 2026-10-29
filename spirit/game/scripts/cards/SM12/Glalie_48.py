from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions


async def drowning_ball(ctx):
    """20 damage; on heads, Paralyze the Defending Pokémon and discard an Energy from it."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Drowning Ball"))[0]
    if not heads:
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.discard_energy_from(
        defender, 1, prompt="Choose an Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="47beaee1-765e-5f0f-bc44-8422dc2c5371",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Ice Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed, and discard an Energy from that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=drowning_ball,
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="This Pok\u00e9mon can't use Frosty Typhoon during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)