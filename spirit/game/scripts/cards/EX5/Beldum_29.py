"""STUB: effect not implemented — do not guess mechanics.
Beldum (EX5 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.attributes import AttrID
from spirit.game.card_effects.ex import poke_power_condition, metal_charge
from spirit.game.session.effects import is_basic_pokemon


async def magnetic_call(ctx):
    results = await ctx.flip_coins(1, "Magnetic Call")
    if not (results and results[0]):
        return
    space = 5 - len(ctx.my_bench())  # typical bench capacity
    if space <= 0:
        await ctx.shuffle_deck()
        return
    picks = await ctx.search_deck(
        _metal_basic, count=1, minimum=0,
        prompt="Choose a Metal Basic Pokémon.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


def _metal_basic(card):
    if not is_basic_pokemon(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    metal = PokemonTypes.METAL.value
    return metal in types or PokemonTypes.METAL in types


card = PokemonCardDef(
    guid="cc645630-883f-50c2-8b0e-21042d609f2e",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Call",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Metal Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Beldum is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=magnetic_call,
        ),
        Attack(
            title="Metal Charge",
            game_text="Put 1 damage counter on Beldum.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=metal_charge(1),
        ),
    ],
)