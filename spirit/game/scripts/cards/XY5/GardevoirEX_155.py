from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive


async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


async def _cavalry_lance(ctx):
    """Printed damage; during your opponent's next turn this Pokémon has no Weakness."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, no_weakness_passive())


card = PokemonCardDef(
    guid="7b3af7c7-ae04-57b2-8ec4-45f462a4b9d4",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    display_name="Gardevoir-EX",
    searchable_by=["Gardevoir-EX", "Basic", "EX", "GardevoirEX"],
    subtypes=["Basic", "EX"],
    collector_number=155,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title="Life Leap",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=gulp_down,
        ),
        Attack(
            title="Shining Wind",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.FAIRY: 3},
            damage=100,
            effect=_cavalry_lance,
        ),
    ],
)