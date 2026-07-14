from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import draw_attack


async def turn_a_profit(ctx):
    """30. If the opponent's Basic is Knocked Out by this damage, take 2 more Prizes."""
    defender = ctx.defender
    was_basic = (
        defender is not None
        and defender.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    )
    await ctx.deal_damage()
    if was_basic and defender in ctx.knockouts:
        ctx.extra_prizes += 2


card = PokemonCardDef(
    guid="85df8316-8135-5eba-ada9-8fb201378dc6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentVMAX.Name",
    display_name="Greedent VMAX",
    searchable_by=["Greedent VMAX", "VMAX", "GreedentVMAX"],
    subtypes=["VMAX"],
    collector_number=218,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentV.Name",
    family_id=820,
    abilities=[
        Attack(
            title="Turn a Profit",
            game_text="If your opponent's Basic Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=turn_a_profit,
        ),
        Attack(
            title="Max Gimme Gimme",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=draw_attack(3),
        ),
    ],
)