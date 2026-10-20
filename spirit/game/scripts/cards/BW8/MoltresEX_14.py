from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import plasma_energy_attached


async def crunch(ctx):
    """30. Flip a coin. If heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="bcb8fcca-4e78-5119-8418-1276a2d53500",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresEX.Name",
    display_name="Moltres-EX",
    searchable_by=["Moltres-EX", "Basic", "EX", "Team Plasma", "MoltresEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=14,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=146,
    abilities=[
        Attack(
            title="Destructive Flame",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=crunch,
        ),
        Attack(
            title="Power Flame",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: bool(plasma_energy_attached(ctx.attacker)), 40),
        ),
    ],
)