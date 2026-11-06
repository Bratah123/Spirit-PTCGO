from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_retreat_cost
from spirit.game.card_effects.attacks_common import bonus_if


async def _iron_crash(ctx):
    """20 more damage for each Colorless in the opponent's Active's Retreat Cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage(20 + 20 * cost)


card = PokemonCardDef(
    guid="af7a3d84-a33e-5cf9-ba1c-fa11d5b42cd3",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1", "Beartic"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Igloo Hold",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=_iron_crash,
        ),
        Attack(
            title="Mountain Drop",
            game_text="If there is any Stadium card in play, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 40),
        ),
    ],
)