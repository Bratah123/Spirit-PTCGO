from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def axe_slash(ctx):
    """Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon."""
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="77f605f7-0d49-54c0-a30c-86433a18731b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    display_name="Kleavor V",
    searchable_by=["Kleavor V", "Basic", "V", "KleavorV"],
    subtypes=["Basic", "V"],
    collector_number=87,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=900,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Axe Slash",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=axe_slash,
        ),
    ],
)