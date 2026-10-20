from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.content.definitions import def_for


async def _fire_spin(ctx):
    """Printed damage. Flip a coin. If tails, discard 2 Energy from this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Fire Spin")
    if results and not results[0]:
        await ctx.discard_energy_from(ctx.attacker, 2)


def _is_m(card):
    return getattr(def_for(card.archetype_id), "display_name", None) == "M Rayquaza-EX"


card = PokemonCardDef(
    guid="3ab789bd-6dcc-5c21-a5d7-c7d85ddbb4cb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=66,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title="Mega Ascension",
            game_text="Search your deck for M Rayquaza-EX, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(_is_m, count=1, minimum=0, reveal=True, prompt="Choose M Rayquaza-EX"),
        ),
        Attack(
            title="Aeroscream",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=_fire_spin,
        ),
    ],
)