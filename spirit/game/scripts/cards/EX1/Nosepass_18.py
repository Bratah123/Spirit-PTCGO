from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import active_is
from spirit.game.card_effects.ex import scoop_defending_to_hand
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_evolution_pokemon

_search_any = search_to_hand(
    count=1, minimum=0, reveal=False,
    prompt="Choose a card to put into your hand.",
)


async def invisible_hand(ctx):
    """If the opponent's Active is an Evolved Pokémon, search any 1 card."""
    if not active_is(is_evolution_pokemon)(ctx):
        return
    await _search_any(ctx)


card = PokemonCardDef(
    guid="b8e539b2-db4a-5b64-8b4b-cdccb63ac4c4",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=299,
    abilities=[
        Attack(
            title="Invisible Hand",
            game_text="If any of your opponent's Active Pok\u00e9mon are Evolved Pok\u00e9mon, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=invisible_hand,
        ),
        Attack(
            title="Repulsion",
            game_text="Flip a coin. If heads, your opponent returns the Defending Pok\u00e9mon and all cards attached to it to his or her hand. (If your opponent doesn't have any Benched Pok\u00e9mon or other Active Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=scoop_defending_to_hand(flip=True),
        ),
    ],
)
