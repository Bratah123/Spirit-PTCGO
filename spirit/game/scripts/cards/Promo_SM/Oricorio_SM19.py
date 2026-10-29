from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.session.effects import is_pokemon_card


async def supernatural_dance(ctx):
    """1 damage counter per Pokémon in the opponent's discard, placed any way."""
    n = sum(1 for c in ctx.discard_pile(ctx.opponent_id) if is_pokemon_card(c))
    if n > 0:
        await ctx.place_damage_counters(n, ctx.opponent_pokemon_in_play())


async def revelation_dance(ctx):
    """30 damage only if a Stadium is in play."""
    if ctx.stadium_in_play() is None:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b8116976-2525-520e-b7bf-474367115a21",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title="Supernatural Dance",
            game_text="For each Pok\u00e9mon in your opponent's discard pile, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=supernatural_dance,
        ),
        Attack(
            title="Revelation Dance",
            game_text="If there is no Stadium card in play, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=revelation_dance,
        ),
    ],
)