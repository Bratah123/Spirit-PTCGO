from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def _ear_influence(ctx):
    """Move as many damage counters on your opponent's Pokemon as you like to
    any of their other Pokemon in any way you like."""
    for _ in range(30):
        damaged = [p for p in ctx.opponent_pokemon_in_play()
                   if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
        others = ctx.opponent_pokemon_in_play()
        if not damaged or len(others) < 2:
            return
        if not await ctx.ask_yes_no("Move damage counters from one of your opponent's Pokémon?"):
            return
        src = await ctx.choose_pokemon(damaged, "Move damage counters from which Pokémon?")
        if src is None:
            return
        avail = (ctx.max_hp(src) - src.get_attribute(AttrID.HP, 0)) // 10
        idx = await ctx.choose("How many damage counters?", [str(i) for i in range(1, avail + 1)])
        moved = await ctx.move_damage_counters(src, [p for p in others if p is not src],
                                               max_count=(idx or 0) + 1)
        if not moved:
            return


card = PokemonCardDef(
    guid="f8ede0d6-57d6-561a-860c-fb90da5fcad6",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Attack(
            title="Ear Influence",
            game_text="Move as many damage counters on your opponent's Pok\u00e9mon as you like to any of your opponent's other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_ear_influence,
        ),
        Attack(
            title="Psychic",
            game_text="Does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=60),
        ),
    ],
)