from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def team_magmas_great_ball_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


def _energy(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def team_magmas_great_ball(ctx):
    """Search your deck for a Basic Team Magma Pokemon and a basic Fighting Energy
    card, reveal them, and put them into your hand; shuffle."""
    found = []
    found += await ctx.search_deck(lambda c: is_basic_pokemon(c) and _team(c, "Magma"), 1, minimum=0,
                                   prompt="Choose a Basic Team Magma Pokémon")
    found += await ctx.search_deck(_energy, 1, minimum=0, prompt="Choose a basic Fighting Energy card")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="489c8b1b-246c-590e-893e-14738017b7d6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasGreatBall.Name",
    display_name="Team Magma's Great Ball",
    searchable_by=["Team Magma's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=31,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_magmas_great_ball_condition,
    effect=team_magmas_great_ball
)
