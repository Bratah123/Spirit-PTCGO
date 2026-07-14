from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.trainers import is_energy_card


async def strobe_shock(ctx):
    """90 damage. Your opponent reveals their hand; if it holds an Energy
    card, their Active Pokemon is now Paralyzed."""
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    if any(is_energy_card(c) for c in hand):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="833a1edb-1f10-5dd4-addc-736fa418350c",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Strobe Shock",
            game_text="Your opponent reveals their hand. If you find any Energy cards there, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=strobe_shock,
        ),
    ],
)
