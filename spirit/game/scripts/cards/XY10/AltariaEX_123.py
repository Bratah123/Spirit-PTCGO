from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive


async def _cavalry_lance(ctx):
    """Printed damage; during your opponent's next turn this Pokémon has no Weakness."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, no_weakness_passive())


async def _powerful_gain(ctx):
    """30+; if this Pokemon was healed this turn, 60 more and heal 30 from it."""
    healed = ctx.attacker.entity_id in ctx.session.turn_state.healed_entities
    await ctx.deal_damage(ctx.ability.damage + (60 if healed else 0))
    if healed:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="0f1ec2c7-b413-55c5-998e-1fc3b76cf7fe",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name",
    display_name="Altaria-EX",
    searchable_by=["Altaria-EX", "Basic", "EX", "AltariaEX"],
    subtypes=["Basic", "EX"],
    collector_number=123,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=334,
    abilities=[
        Attack(
            title="Powerful Gain",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 60 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=_powerful_gain,
        ),
        Attack(
            title="Shining Wind",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_cavalry_lance,
        ),
    ],
)