from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


async def _turbo_energize(ctx):
    """Search your deck for 2 basic Energy cards and attach them to your
    Benched Pokemon in any way you like; shuffle."""
    bench = ctx.my_bench()
    if bench:
        picks = await ctx.search_deck(is_basic_energy_card, count=2, minimum=0,
                                      prompt="Choose up to 2 basic Energy cards to attach")
        if picks:
            await distribute_energy(ctx, picks, bench)
    await ctx.shuffle_deck()


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


card = PokemonCardDef(
    guid="44a957de-5afe-50da-b2c9-6efef376de54",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniEX.Name",
    display_name="Victini-EX",
    searchable_by=["Victini-EX", "Basic", "EX", "VictiniEX"],
    subtypes=["Basic", "EX"],
    collector_number=131,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Turbo Energize",
            game_text="Search your deck for 2 basic Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=_turbo_energize,
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: _is_pokemon_ex(ctx.defender), 50),
        ),
    ],
)