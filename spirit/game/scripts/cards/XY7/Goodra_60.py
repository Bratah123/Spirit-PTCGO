from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_retreat_cost
from spirit.game.card_effects.passives_common import condition_immunity_passive


async def _liquid_blow(ctx):
    """20 to 1 of your opponent's Pokemon for each Colorless in its Retreat Cost."""
    opp = ctx.opponent_pokemon_in_play()
    if not opp:
        return
    target = opp[0] if len(opp) == 1 else await ctx.choose_pokemon(opp, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        n = effective_retreat_cost(ctx.board, target)
        if n > 0:
            await ctx.deal_damage(20 * n, target=target)


async def _shining_breath(ctx):
    """110; during your opponent's next turn this Pokemon can't be affected by Special Conditions."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, condition_immunity_passive())


card = PokemonCardDef(
    guid="b1d9b19c-7e4c-5131-b59a-fbde46b87acf",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Liquid Blow",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Colorless in its Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_liquid_blow,
        ),
        Attack(
            title="Shining Breath",
            game_text="During your opponent's next turn, this Pok\u00e9mon can't be affected by any Special Conditions.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=_shining_breath,
        ),
    ],
)