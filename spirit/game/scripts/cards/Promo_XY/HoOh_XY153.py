from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _stoke(ctx):
    """Flip a coin. If heads, attach up to 2 Fire Energy cards from your deck to this Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
    picks = await ctx.search_deck(_is_fire_energy, count=2, minimum=0,
                                  prompt="Choose up to 2 Fire Energy cards")
    for card in picks or []:
        await ctx.attach_energy(card, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="03cad2ae-d04f-5fba-89a1-9090832badd5",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title="Stoke",
            game_text="Flip a coin. If heads, search your deck for up to 2 Fire Energy cards and attach them to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_stoke,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)