from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.attacks_common import damage_per


async def _bright_look(ctx):
    """On evolve: you may switch 1 of your opponent's Benched Pokemon with their Active."""
    bench = ctx.opponent_bench()
    if not bench or not await ctx.ask_yes_no("Switch in 1 of your opponent's Benched Pok\u00e9mon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose your opponent's new Active Pok\u00e9mon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def _defender_condition_count(ctx):
    d = ctx.defender
    return len(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if d is not None else 0


card = PokemonCardDef(
    guid="67cde530-2f3c-5c18-8e9f-8600dee504ca",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Bright Look",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_bright_look,
        ),
        Attack(
            title="Hexed Flame",
            game_text="Does 50 more damage for each Special Condition affecting the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(_defender_condition_count, 50, base=20),
        ),
    ],
)