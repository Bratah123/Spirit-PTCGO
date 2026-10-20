from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import snipe_attack


def _is_ex(card):
    return "EX" in (getattr(def_for(card.archetype_id), "subtypes", None) or [])


async def _scoundrel_ring(ctx):
    """On bench from hand: you may search for up to 3 Pokemon-EX (except Hoopa-EX)."""
    if not ctx.deck() or not await ctx.ask_yes_no("Use Scoundrel Ring?"):
        return
    picks = await ctx.search_deck(
        lambda c: is_pokemon_card(c) and _is_ex(c)
        and getattr(def_for(c.archetype_id), "display_name", None) != "Hoopa-EX",
        count=3, minimum=0, prompt="Choose up to 3 Pokémon-EX")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


_snipe_100 = snipe_attack(100, pool='any')


async def _hyperspace_fury(ctx):
    """Discard 2 Energy attached to this Pokemon; 100 to 1 of your opponent's Pokemon."""
    await ctx.discard_energy_from(ctx.attacker, 2, minimum=2, prompt="Discard 2 Energy")
    await _snipe_100(ctx)


card = PokemonCardDef(
    guid="804f9b37-b361-5620-a1fa-e9337edd69c0",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name",
    display_name="Hoopa-EX",
    searchable_by=["Hoopa-EX", "Basic", "EX", "HoopaEX"],
    subtypes=["Basic", "EX"],
    collector_number=71,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Ability(
            title="Scoundrel Ring",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may search your deck for up to 3 Pok\u00e9mon-EX (except for Hoopa-EX), reveal them, and put them into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=_scoundrel_ring,
        ),
        Attack(
            title="Hyperspace Fury",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 100 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=_hyperspace_fury,
        ),
    ],
)