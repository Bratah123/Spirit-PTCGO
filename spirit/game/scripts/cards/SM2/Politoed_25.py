from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play
from spirit.game.attributes import AttrID


from spirit.game.session.effects import is_pokemon_card


def _named(name):
    def pred(card):
        return is_pokemon_card(card) and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == name
    return pred


async def roll_call(ctx):
    """Search for a Poliwag, a Poliwhirl, and a Poliwrath onto your Bench."""
    groups = await ctx.search_deck_groups(
        [
            (_named("Poliwag"), 1, "Poliwag"),
            (_named("Poliwhirl"), 1, "Poliwhirl"),
            (_named("Poliwrath"), 1, "Poliwrath"),
        ],
        prompt="Choose a Poliwag, a Poliwhirl, and a Poliwrath",
    )
    for group in groups:
        for card in group:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8c2c52cb-51c3-5da5-a799-f226be89032f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=186,
    abilities=[
        Attack(
            title="Roll Call",
            game_text="Search your deck for a Poliwag, a Poliwhirl, and a Poliwrath, and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=roll_call,
        ),
        Attack(
            title="Hyper Jump",
            game_text="You may shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=remove_self_from_play('deck', optional=True),
        ),
    ],
)