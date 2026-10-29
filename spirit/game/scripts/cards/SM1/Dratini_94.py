from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID


def _named(logic_name):
    return lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == logic_name


async def _signs_of_evolution(ctx):
    """Search your deck for a Dratini, a Dragonair, and a Dragonite; reveal; shuffle."""
    groups = await ctx.search_deck_groups(
        [(_named("Dratini"), 1, "Dratini"), (_named("Dragonair"), 1, "Dragonair"),
         (_named("Dragonite"), 1, "Dragonite")],
        prompt="Choose a Dratini, a Dragonair, and a Dragonite",
    )
    picks = [c for g in groups for c in g]
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="6df72a09-57c2-5077-b985-be59bef7965a",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for a Dratini, a Dragonair, and a Dragonite, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=_signs_of_evolution,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)