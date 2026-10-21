from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def team_aquas_great_ball_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


def _energy(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def team_aquas_great_ball(ctx):
    """Search your deck for a Basic Team Aqua Pokemon and a basic Water Energy
    card, reveal them, and put them into your hand; shuffle."""
    found = []
    found += await ctx.search_deck(lambda c: is_basic_pokemon(c) and _team(c, "Aqua"), 1, minimum=0,
                                   prompt="Choose a Basic Team Aqua Pokémon")
    found += await ctx.search_deck(_energy, 1, minimum=0, prompt="Choose a basic Water Energy card")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="67503eb2-c932-5f2f-8aca-6f0c3aea29b6",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasGreatBall.Name",
    display_name="Team Aqua's Great Ball",
    searchable_by=["Team Aqua's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=27,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_aquas_great_ball_condition,
    effect=team_aquas_great_ball
)
