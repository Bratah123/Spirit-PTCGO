from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def _super_deep_dive(ctx):
    """Heal 40 damage from this Pokemon; switch it with 1 of your Benched Pokemon."""
    await ctx.heal(40, ctx.attacker)
    bench = ctx.my_bench()
    if bench:
        t = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if t is not None:
            await ctx.switch_active(ctx.player_id, t)


card = PokemonCardDef(
    guid="aaee9ebc-9d4b-5382-bcd5-83bd23122430",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Super Deep Dive",
            game_text="Heal 40 damage from this Pok\u00e9mon. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=_super_deep_dive,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=recoil_attack(20),
        ),
    ],
)