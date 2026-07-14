from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def electro_wheel(ctx):
    await ctx.deal_damage()
    picks = await ctx.discard_energy_from(ctx.attacker, 1, prompt="Discard an Energy from this Pokémon.")
    if not picks:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)

card = PokemonCardDef(
    guid="8813cb5b-84e5-53d0-a934-e29de452ef45",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoV.Name",
    display_name="Morpeko V",
    searchable_by=["Morpeko V", "Basic", "V", "MorpekoV"],
    subtypes=["Basic", "V"],
    collector_number=79,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Attack(
            title="Spark",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snipe_attack(20, pool="bench", count=1, also_base=True),
        ),
        Attack(
            title="Electro Wheel",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=electro_wheel,
        ),
    ],
)