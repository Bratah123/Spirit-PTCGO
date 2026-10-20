from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _ember(ctx):
    """20; flip: tails discard a Fire Energy attached to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]) and any(_is_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        await ctx.discard_energy_from(ctx.attacker, 1, predicate=_is_fire_energy, minimum=1,
                                      prompt="Discard a Fire Energy")


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _flare_bonus(ctx):
    """Discard a Fire Energy card from your hand. If you do, draw 3 cards."""
    gone = await ctx.discard_from_hand(1, minimum=0, predicate=_is_fire_energy,
                                       prompt="Discard a Fire Energy card")
    if gone:
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="4b961dc2-f6c7-5f8c-9a4b-b56b9333dfca",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesEX.Name",
    display_name="Ninetales-EX",
    searchable_by=["Ninetales-EX", "Basic", "EX", "NinetalesEX"],
    subtypes=["Basic", "EX"],
    collector_number=13,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=38,
    abilities=[
        Attack(
            title="Flare Bonus",
            game_text="Discard a Fire Energy card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.FIRE: 1},
            effect=_flare_bonus,
        ),
        Attack(
            title="Fire Blast",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=_ember,
        ),
    ],
)