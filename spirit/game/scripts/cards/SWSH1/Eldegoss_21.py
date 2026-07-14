from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.card_effects.support_common import distribute_energy


async def blessing_of_fluff(ctx):
    """Search your deck for up to 3 Grass Energy cards and attach them to
    your Benched Pokemon in any way you like. Then, shuffle your deck."""
    picks = await ctx.search_deck(
        is_grass_energy_card, count=3, minimum=0,
        prompt="Choose up to 3 Grass Energy cards to attach to your Benched Pokémon.",
    )
    bench = ctx.my_bench()
    if picks and bench:
        await distribute_energy(ctx, picks, bench)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9ddf1965-4497-59ac-949c-0fec6ad61a9a",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eldegoss.Name",
    display_name="Eldegoss",
    searchable_by=["Eldegoss", "Stage 1", "Eldegoss"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    family_id=829,
    abilities=[
        Attack(
            title="Blessing of Fluff",
            game_text="Search your deck for up to 3 Grass Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=blessing_of_fluff,
        ),
        Attack(
            title="Leafage",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)