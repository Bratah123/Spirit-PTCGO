from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def ghostly_cries(ctx):
    """1 counter per opponent's discarded Pokemon, any way; if any, shuffle those Pokemon into their deck."""
    opponent = ctx.opponent_id
    discard = ctx.discard_pile(opponent)
    pokemon_cards = [c for c in discard if is_pokemon_card(c)]
    count = len(pokemon_cards)
    if count <= 0:
        return
    await ctx.place_damage_counters(count, candidates=ctx.opponent_pokemon_in_play())
    await ctx.shuffle_into_deck(pokemon_cards, player_id=opponent)


card = PokemonCardDef(
    guid="95a51d07-4ea7-5ced-8a3f-789e259f7aac",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Ghostly Cries",
            game_text="For each Pok\u00e9mon in your opponent's discard pile, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like. If you placed any damage counters in this way, your opponent shuffles all Pok\u00e9mon from their discard pile into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ghostly_cries,
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)