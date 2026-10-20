from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def _magnetic_lines(ctx):
    """Printed damage; you may move an Energy from the Defending Pokemon to
    1 of your opponent's Benched Pokemon."""
    await ctx.deal_damage()
    defender, bench = ctx.defender, ctx.opponent_bench()
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    picks = await ctx.choose_cards(energies, 1, minimum=0,
                                   prompt="You may choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pok\u00e9mon to move it to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="51e76940-9988-5bae-91f3-55d619a2925b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Magnetic Lines",
            game_text="You may move an Energy attached to the Defending Pok\u00e9mon to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_magnetic_lines,
        ),
        Attack(
            title="Heavy Nose",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage(), 30),
        ),
    ],
)