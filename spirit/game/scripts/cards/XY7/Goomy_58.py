from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_bench_capacity


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _water_down(ctx):
    """When you attach a Water Energy from hand to this Pokemon, you may
    search your deck for Goomy and put it onto your Bench."""
    if (ctx.energy_receiver is not ctx.source or ctx.attaching_player_id != ctx.player_id
            or not _is_water_energy(ctx.attached_energy)):
        return
    if len(ctx.my_bench()) >= effective_bench_capacity(ctx.board, ctx.player_id):
        return
    if not await ctx.ask_yes_no("Search your deck for Goomy and put it onto your Bench?"):
        return
    picks = await ctx.search_deck(lambda c: getattr(def_for(c.archetype_id), "display_name", None) == "Goomy",
                                  count=1, minimum=0, prompt="Choose a Goomy")
    if picks:
        await ctx.bench_pokemon(picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ac380742-d1d1-5069-b32d-c4c4b648ec23",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic", "Goomy"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=704,
    abilities=[
        Ability(
            title="Water Down",
            game_text="Whenever you attach a Water Energy card from your hand to this Pok\u00e9mon, you may search your deck for Goomy and put it onto your Bench. Shuffle your deck afterward.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_water_down,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)