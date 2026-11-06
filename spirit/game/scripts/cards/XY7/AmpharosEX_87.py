from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _thunder_rod(ctx):
    """Look at the top 4 cards; attach any Lightning Energy there to this Pokemon; shuffle."""
    top = ctx.deck_top(4)
    pool = [c for c in top if _is_lightning_energy(c)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, display_cards=top,
                                   prompt="Attach Lightning Energy to this Pokémon") if pool else []
    for energy in picks or []:
        await ctx.attach_energy(energy, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="2988501b-19c3-5491-a1bc-4dc6ecef3aa7",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name",
    display_name="Ampharos-EX",
    searchable_by=["Ampharos-EX", "Basic", "EX", "AmpharosEX"],
    subtypes=["Basic", "EX"],
    collector_number=87,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=181,
    abilities=[
        Attack(
            title="Thunder Rod",
            game_text="Look at the top 4 cards of your deck and attach as many Lightning Energy cards you find there as you like to this Pok\u00e9mon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_thunder_rod,
        ),
        Attack(
            title="Sparkling Tail",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)