from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.support_common import attach_from_discard, requires_bench_space
from spirit.game.card_effects.trainers import is_basic_energy_card


async def reviving_flame(ctx):
    """Once per turn from discard: you may Bench this Pokémon, then attach up
    to 4 basic Energy from discard to it. Using this Ability ends your turn."""
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    ctx.ends_turn = True
    await attach_from_discard(predicate=is_basic_energy_card, count=4,
                               target="self", minimum=0)(ctx)


def _basic_energy_types_count(ctx):
    types = set()
    for e in ctx.attached_energies(ctx.attacker):
        if is_basic_energy_card(e):
            for t in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(t)
    return len(types)


card = PokemonCardDef(
    guid="1c0e13b7-d61c-50d2-9677-915ded60d739",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhV.Name",
    display_name="Ho-Oh V",
    searchable_by=["Ho-Oh V", "Basic", "V", "HoOhV"],
    subtypes=["Basic", "V"],
    collector_number=187,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Ability(
            title="Reviving Flame",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, attach up to 4 basic Energy cards from your discard pile to this Pok\u00e9mon. If you use this Ability, your turn ends.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=reviving_flame,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="This attack does 30 more damage for each type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=damage_per(_basic_energy_types_count, 30, base=100),
        ),
    ],
)