from spirit.game.data_utils import PokemonCardDef, Attack, Ability, has_rule_box
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import (
    ability_lock_passive, is_in_active_spot, opposing_pokemon,
)
from spirit.game.session.effects import is_basic_pokemon


def _emperors_eyes_target(pokemon, carrier):
    return (
        is_in_active_spot(carrier)
        and opposing_pokemon(pokemon, carrier)
        and is_basic_pokemon(pokemon)
        and not has_rule_box(pokemon.archetype_id)
    )


async def swirling_slice(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to move to 1 of your Benched Pokémon"
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to"
    )
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="9c5935c1-0362-50df-aabc-4370364a48b3",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonV.Name",
    display_name="Empoleon V",
    searchable_by=["Empoleon V", "Basic", "V", "Rapid Strike", "EmpoleonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=40,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=395,
    abilities=[
        Ability(
            title="Emperor's Eyes",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Basic Pok\u00e9mon in play have no Abilities, except for Pok\u00e9mon with a Rule Box (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes).",
            passive=ability_lock_passive(_emperors_eyes_target),
        ),
        Attack(
            title="Swirling Slice",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=swirling_slice,
        ),
    ],
)