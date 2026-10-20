from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _aqua_search_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def _aqua_search(ctx):
    """Search your deck for a Team Aqua Pokemon, reveal it, put it into your hand; shuffle."""
    await search_to_hand(lambda c: is_pokemon_card(c) and _team(c, "Aqua"), count=1, minimum=0,
                         reveal=True, prompt="Choose a Team Aqua Pokémon")(ctx)


card = PokemonCardDef(
    guid="ea310bb7-e045-55c5-a408-d5b37ecfbc02",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSharpedo.Name",
    display_name="Team Aqua's Sharpedo",
    searchable_by=["Team Aqua's Sharpedo", "Stage 1", "TeamAquasSharpedo"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Aqua Search",
            game_text="Once during your turn (before your attack), you may search your deck for a Team Aqua Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_aqua_search_condition,
            effect=_aqua_search,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)