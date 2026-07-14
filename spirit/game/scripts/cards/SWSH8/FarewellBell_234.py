from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import is_pokemon_vmax


async def _farewell_bell(ctx):
    if not ctx.ko_from_attack or not is_pokemon_vmax(ctx.source.archetype_id):
        return
    picks = await ctx.search_deck(
        count=1, minimum=0, prompt="Choose a card to put into your hand."
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="d6236064-cf7a-506a-95b6-b7db157d0dea",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FarewellBell.Name",
    display_name="Farewell Bell",
    searchable_by=["Farewell Bell", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00c3\u00a9mon Tool"],
    collector_number=234,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Farewell Bell",
            game_text="If the Pok\u00e9mon VMAX this card is attached to is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_farewell_bell,
        ),
    ],
)
