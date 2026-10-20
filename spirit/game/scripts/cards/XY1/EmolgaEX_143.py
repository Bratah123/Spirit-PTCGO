from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import discard_for_bonus


def _is_lightning_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _energy_glide(ctx):
    """Search your deck for a Lightning Energy card and attach it to this
    Pokemon; shuffle. If you attached Energy this way, switch this Pokemon
    with 1 of your Benched Pokemon."""
    picks = await ctx.search_deck(_is_lightning_energy_card, count=1, minimum=0,
                                  prompt="Choose a Lightning Energy card")
    attached = False
    for card in picks or []:
        await ctx.attach_energy(card, ctx.attacker)
        attached = True
    await ctx.shuffle_deck()
    bench = ctx.my_bench()
    if attached and bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="4c5521dd-6631-57a5-b638-a8398fffa469",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmolgaEX.Name",
    display_name="Emolga-EX",
    searchable_by=["Emolga-EX", "Basic", "EX", "EmolgaEX"],
    subtypes=["Basic", "EX"],
    collector_number=143,
    set_code="XY1",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=587,
    abilities=[
        Attack(
            title="Energy Glide",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward. If you attached Energy in this way, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_glide,
        ),
        Attack(
            title="Electron Crush",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=discard_for_bonus(source='self-energy', max_count=1, flat=30,
                prompt='Discard an Energy for 30 more damage?'),
        ),
    ],
)