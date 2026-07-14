from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.card_effects.support_common import distribute_energy


async def attach_leaves(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    cards = [c for c in ctx.discard_pile() if is_grass_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Choose up to 2 Grass Energy cards to attach to your Benched Pokémon",
    )
    if not picks:
        return
    await distribute_energy(ctx, picks, bench)


card = PokemonCardDef(
    guid="93ae08e5-6541-5b28-9c6b-99a77d28f1d7",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Attach Leaves",
            game_text="Attach up to 2 Grass Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_leaves,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)