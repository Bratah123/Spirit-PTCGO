from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _purifying_flame(ctx):
    """Printed damage; remove all Special Conditions from this Pokemon."""
    await ctx.deal_damage()
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="9248636b-4af2-52e0-9019-713ddbaedf78",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic", "Swirlix"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=684,
    abilities=[
        Attack(
            title="Lick Away",
            game_text="Remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_purifying_flame,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)