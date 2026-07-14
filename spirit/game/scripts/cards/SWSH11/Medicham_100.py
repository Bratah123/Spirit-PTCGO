from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.pokemon import energy_provides_type


async def battle_step(ctx):
    """50 damage. Search your deck for up to 2 Fighting Energy cards and
    attach them to your Benched Pokemon in any way you like. Then, shuffle."""
    await ctx.deal_damage()
    picks = await ctx.search_deck(
        lambda c: energy_provides_type(c, PokemonTypes.FIGHTING.value),
        count=2, minimum=0,
        prompt="Choose up to 2 Fighting Energy cards to attach.",
    )
    bench = ctx.my_bench()
    if picks and bench:
        await distribute_energy(ctx, picks, bench)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="7313494d-5c08-5313-8bce-4994e996457c",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Battle Step",
            game_text="Search your deck for up to 2 Fighting Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=battle_step,
        ),
    ],
)