from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _biosmog(ctx):
    """Printed damage; the Defending Pokemon is now Poisoned. Flip a coin; if
    heads, discard an Energy attached to it."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is None or ctx.effects_blocked(d):
        return
    await ctx.apply_special_condition(d, SpecialConditions.POISONED)
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0] and ctx.attached_energies(d):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="a4a2a152-f8ec-58a2-bfea-a273634228ab",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Team Plasma", "Garbodor"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=66,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Biosmog",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Flip a coin. If heads, discard an Energy attached to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_biosmog,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)