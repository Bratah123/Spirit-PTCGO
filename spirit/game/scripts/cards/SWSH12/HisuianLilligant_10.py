from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_grass_energy_card


async def swelling_scent(ctx):
    picks = await ctx.search_deck(
        is_grass_energy_card, count=2, minimum=0,
        prompt="Choose up to 2 Grass Energy cards to attach.",
    )
    if picks:
        bench = ctx.my_bench()
        if bench:
            await distribute_energy(ctx, picks, bench)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d21fafd9-95be-55db-88e0-51508533fc03",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligant.Name",
    display_name="Hisuian Lilligant",
    searchable_by=["Hisuian Lilligant", "Stage 1", "HisuianLilligant"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Swelling Scent",
            game_text="Search your deck for up to 2 Grass Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={},
            effect=swelling_scent,
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)