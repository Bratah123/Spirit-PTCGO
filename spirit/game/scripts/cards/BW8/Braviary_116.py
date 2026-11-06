from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import opponent_switches


async def superpower(ctx):
    """You may do 20 more damage; if you do, this Pokémon does 20 to itself."""
    if await ctx.ask_yes_no(
        "Do 20 more damage? If you do, this Pokémon does 20 damage to itself."
    ):
        await ctx.deal_damage(80)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(60)


def _big_wing_condition(board, player_id, pokemon=None):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opponent, "bench") if opponent else None
    return (pokemon is not None and pokemon is board.active_pokemon(player_id)
            and bool(bench and bench.children))


async def _big_wing(ctx):
    """If this Pokemon is your Active, your opponent switches their Active
    with 1 of their Benched Pokemon."""
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="2b4d114d-a723-5e1b-9d91-e67d56199a7c",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1", "Braviary"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Ability(
            title="Big Wing",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_big_wing_condition,
            effect=_big_wing,
        ),
        Attack(
            title="Wild Edge",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=superpower,
        ),
    ],
)