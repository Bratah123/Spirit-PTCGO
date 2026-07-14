from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_evolution_pokemon


def _evolves_from_fossil(card) -> bool:
    d = def_for(card.archetype_id)
    return bool(d) and bool(getattr(d, "evolves_from", None)) and "Fossil" in d.evolves_from


async def tentacle_lock(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_evolution_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="951e64dd-a4a5-5e95-aca2-3b0e9d2247c3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OmastarV.Name",
    display_name="Omastar V",
    searchable_by=["Omastar V", "Basic", "V", "OmastarV"],
    subtypes=["Basic", "V"],
    collector_number=35,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=139,
    abilities=[
        Attack(
            title="Primal Guidance",
            game_text="Search your deck for up to 2 Pok\u00e9mon that evolve from an Item card that has \"Fossil\" in its name and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(predicate=_evolves_from_fossil, count=2),
        ),
        Attack(
            title="Tentacle Lock",
            game_text="If the Defending Pok\u00e9mon is an Evolution Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=tentacle_lock,
        ),
    ],
)