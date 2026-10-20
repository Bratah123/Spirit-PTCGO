from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.session.effects import is_pokemon_card


def _is_water(pokemon):
    return PokemonTypes.WATER.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _life_saver(ctx):
    """Put 2 Water Pokemon from your discard pile into your hand."""
    cards = [c for c in ctx.discard_pile() if is_pokemon_card(c) and _is_water(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 2, minimum=min(2, len(cards)), prompt="Choose 2 Water Pokémon")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="d919bf7e-5bba-5392-8180-23395a18f296",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Attack(
            title="Deep Sea Swirl",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Life Saver",
            game_text="Put 2 Water Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.WATER: 1},
            effect=_life_saver,
        ),
    ],
)