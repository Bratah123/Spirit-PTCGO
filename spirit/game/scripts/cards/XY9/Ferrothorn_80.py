from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_retreat_cost


async def _spike_lash(ctx):
    """10 to each opposing Pokemon per Colorless in its Retreat Cost."""
    for p in list(ctx.opponent_pokemon_in_play()):
        n = effective_retreat_cost(ctx.board, p)
        if n:
            await ctx.deal_damage(10 * n, target=p)


card = PokemonCardDef(
    guid="55f307fa-302e-50c1-b0ad-193c715f5f82",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Spike Lash",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon for each Colorless in that Pok\u00e9mon's Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            effect=_spike_lash,
        ),
    ],
)