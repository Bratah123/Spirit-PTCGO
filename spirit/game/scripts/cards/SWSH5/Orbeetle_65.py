from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.session.constants import BENCH_CAPACITY


def _stage2_not_orbeetle(card):
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
        and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != "Orbeetle"
    )


async def evomancy(ctx):
    """For each Energy attached to this Pokémon, search a Stage 2 Pokémon
    (except Orbeetle) onto the Bench. Then, shuffle the deck."""
    count = count_energy("self")(ctx)
    space = BENCH_CAPACITY - len(ctx.my_bench())
    take = min(count, space)
    if take > 0:
        picks = await ctx.search_deck(
            _stage2_not_orbeetle, count=take, minimum=0,
            prompt="Choose Stage 2 Pokémon to put onto your Bench.",
        )
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="cae6af0b-3116-57b0-83bb-99cd9619cae0",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Evomancy",
            game_text="For each Energy attached to this Pokémon, search your deck for a Stage 2 Pokémon, except Orbeetle, and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=evomancy,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
