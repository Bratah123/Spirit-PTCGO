from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _diving_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def _diving_search(ctx):
    """Search your deck for a card; shuffle, then put that card on top."""
    picks = await ctx.search_deck(lambda c: True, count=1, minimum=0, prompt="Choose a card")
    await ctx.shuffle_deck()
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="bb2a8636-dec1-5754-89da-baa24c43b17e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        ancient_trait('α Growth'),
        Ability(
            title="Diving Search",
            game_text="Once during your turn (before your attack), you may search your deck for a card. Shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_diving_condition,
            effect=_diving_search,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.WATER), 30, base=40),
        ),
    ],
)