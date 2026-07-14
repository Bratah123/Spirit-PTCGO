from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.attacks_common import recoil_attack


async def assisting_spark(ctx):
    """30 damage. You may attach a Lightning Energy card from your hand to
    1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    energies = [c for c in ctx.hand() if energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Attach a Lightning Energy card from your hand to 1 of your Benched Pokémon?"
    ):
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose a Lightning Energy card to attach.")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon.")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="cc401b1c-80d0-5ed1-b895-eb9c92dbbf1e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Assisting Spark",
            game_text="You may attach a Lightning Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=assisting_spark,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=recoil_attack(30),
        ),
    ],
)