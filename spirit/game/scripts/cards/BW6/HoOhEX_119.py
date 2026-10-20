from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import damage_per


async def _rebirth(ctx):
    """From the discard pile: flip; if heads Bench this Pokemon and attach 3
    different types of basic Energy from the discard pile to it."""
    results = await ctx.flip_coins(1, "Rebirth")
    if not results or not results[0]:
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    used = set()
    for _ in range(3):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)
                and not (set(c.get_attribute(AttrID.POKEMON_TYPES) or []) & used)]
        if not pool:
            break
        picks = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a basic Energy of a different type to attach")
        if not picks:
            break
        used.update(picks[0].get_attribute(AttrID.POKEMON_TYPES) or [])
        await ctx.attach_energy(picks[0], ctx.source)


def _basic_energy_type_count(ctx):
    types = set()
    for e in ctx.attached_energies(ctx.attacker):
        if is_basic_energy_card(e):
            types.update(e.get_attribute(AttrID.POKEMON_TYPES) or [])
    return len(types)


card = PokemonCardDef(
    guid="3ffcaaa9-d569-51fd-9810-eb4337a57a7f",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name",
    display_name="Ho-Oh-EX",
    searchable_by=["Ho-Oh-EX", "Basic", "EX", "HoOhEX"],
    subtypes=["Basic", "EX"],
    collector_number=119,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Rebirth",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may flip a coin. If heads, put this Pok\u00e9mon onto your Bench and attach 3 different types of basic Energy cards from the discard pile to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=_rebirth,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 20 more damage for each different type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=damage_per(_basic_energy_type_count, 20, base=20),
        ),
    ],
)