from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def _iron_crusher(ctx):
    """120; you may discard a Special Energy from the opponent's Active or a Stadium in play."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    specials = [e for e in ctx.attached_energies(d) if is_special_energy(e)] if d is not None else []
    if d is not None and ctx.effects_blocked(d):
        specials = []
    options = []
    if specials:
        options.append("Discard a Special Energy")
    if ctx.stadium_in_play() is not None:
        options.append("Discard the Stadium")
    if not options:
        return
    pick = await ctx.choose("Iron Crusher", options + ["Do nothing"], use_panel=False)
    if pick >= len(options):
        return
    if options[pick].endswith("Stadium"):
        await ctx.discard_stadium()
    else:
        chosen = await ctx.choose_cards(specials, 1, minimum=1, prompt="Choose a Special Energy to discard")
        if chosen:
            await ctx.discard_cards(chosen)


card = PokemonCardDef(
    guid="7f940ad9-d5e3-58f1-bb80-d2c871785c37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MScizorEX.Name",
    display_name="M Scizor-EX",
    searchable_by=["M Scizor-EX", "MEGA", "EX", "MScizorEX"],
    subtypes=["MEGA", "EX"],
    collector_number=120,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name",
    family_id=212,
    abilities=[
        Attack(
            title="Iron Crusher",
            game_text="You may discard a Special Energy attached to your opponent's Active Pok\u00e9mon or a Stadium card in play.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            effect=_iron_crusher,
        ),
    ],
)