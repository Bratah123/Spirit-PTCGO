from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


async def _wake_up_beam(ctx):
    """Printed damage; remove all Special Conditions from the Defending Pokemon."""
    await ctx.deal_damage()
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.cure_all_conditions(ctx.defender)


card = PokemonCardDef(
    guid="26b8018c-24c0-508f-a992-b67366f8c998",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Wake-up Beam",
            game_text="Remove all Special Conditions from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_wake_up_beam,
        ),
        Attack(
            title="Drain Slap",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=heal_attack(30),
        ),
    ],
)