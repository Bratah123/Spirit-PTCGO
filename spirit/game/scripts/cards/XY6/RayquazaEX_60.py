from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _dragon_strike(ctx):
    """130; flip: tails, this Pokemon can't use Dragon Strike during your next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and not results[0]:
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, ctx.ability.ability_id)


card = PokemonCardDef(
    guid="4c8c1f46-216b-5ef9-ab9c-179d80cc30a4",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=60,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Dragon Strike",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_dragon_strike,
        ),
    ],
)