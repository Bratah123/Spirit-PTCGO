from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import is_energy_card


async def _precious_touch(ctx):
    bench = ctx.my_bench()
    hand_energy = [c for c in ctx.hand() if is_energy_card(c)]
    if not bench or not hand_energy:
        return
    picks = await ctx.choose_cards(hand_energy, 1, prompt="Choose an Energy card to attach.")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon.")
    if target is None:
        return
    if await ctx.attach_energy(picks[0], target):
        await ctx.heal(120, target=target)


def _distinct_bench_types(ctx) -> int:
    types = set()
    for pokemon in ctx.my_bench():
        for t in pokemon.get_attribute(AttrID.POKEMON_TYPES) or []:
            types.add(t)
    return len(types)


card = PokemonCardDef(
    guid="3a32d55c-0bd7-52a6-984b-6bbae1da07e2",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonVMAX.Name",
    display_name="Sylveon VMAX",
    searchable_by=["Sylveon VMAX", "VMAX", "Rapid Strike", "SylveonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=212,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonV.Name",
    family_id=700,
    abilities=[
        Attack(
            title="Precious Touch",
            game_text="Attach an Energy card from your hand to 1 of your Benched Pok\u00e9mon. If you do, heal 120 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_precious_touch,
        ),
        Attack(
            title="Max Harmony",
            game_text="This attack does 30 more damage for each different type of Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(_distinct_bench_types, 30, base=70),
        ),
    ],
)