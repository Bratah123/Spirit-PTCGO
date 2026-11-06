from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_tool
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fairy_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FAIRY.value)


async def _precious_ribbon(ctx):
    """100; move a Fairy Energy from this Pokemon to 1 of your Benched Pokemon;
    if you do, heal 50 damage from that Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench or not any(_is_fairy_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        return
    moved = await ctx.move_energy_freely([ctx.attacker], bench, predicate=_is_fairy_energy, max_count=1,
                                         prompt="Move a Fairy Energy to a Benched Pokémon")
    for _e, dest in moved or []:
        await ctx.heal(50, dest)


card = PokemonCardDef(
    guid="0af78f68-3867-5101-abce-eba0426f37ab",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonEX.Name",
    display_name="Sylveon-EX",
    searchable_by=["Sylveon-EX", "Basic", "EX", "SylveonEX"],
    subtypes=["Basic", "EX"],
    collector_number=104,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=700,
    abilities=[
        Attack(
            title="Dress Up",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: has_tool(ctx.attacker), 30),
        ),
        Attack(
            title="Precious Ribbon",
            game_text="Move a Fairy Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. If you do, heal 50 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_precious_ribbon,
        ),
    ],
)