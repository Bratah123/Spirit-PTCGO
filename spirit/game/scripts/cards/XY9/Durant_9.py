from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.session.passives import effective_max_hp


async def _scrape_down(ctx):
    """If this Pokemon has any damage counters, discard the top 4 cards of your opponent's deck."""
    me = ctx.attacker
    if effective_max_hp(ctx.board, me) > me.get_attribute(AttrID.HP, 0):
        await ctx.discard_cards(ctx.deck_top(4, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="e92e0e0b-a002-569d-a8bb-24d64c1874cf",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Attack(
            title="Mountain Munch",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=mill_attack(1),
        ),
        Attack(
            title="Scrape Down",
            game_text="If this Pok\u00e9mon has any damage counters on it, discard the top 4 cards of your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=_scrape_down,
        ),
    ],
)