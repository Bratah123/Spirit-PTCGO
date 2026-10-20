from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def _charge_beam(ctx):
    """Printed damage. Flip a coin. If heads, attach an Energy card from your
    discard pile to this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Charge Beam")
    if not results or not results[0]:
        return
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="49e9f325-fd73-5c8a-8de6-f32ae43b9277",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_charge_beam,
        ),
    ],
)