from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.trainers import is_basic_energy_card


_POWDER = [("Asleep", SpecialConditions.ASLEEP), ("Poisoned", SpecialConditions.POISONED)]


async def _conversion_powder(ctx):
    """Choose Asleep or Poisoned for the opponent's Active Pokemon."""
    target = ctx.defender
    if target is None:
        return
    idx = await ctx.choose("Choose a Special Condition", [n for n, _ in _POWDER])
    await ctx.apply_special_condition(target, _POWDER[idx or 0][1])


def _basic_energy_types_count(ctx):
    types = set()
    for e in ctx.attached_energies(ctx.attacker):
        if is_basic_energy_card(e):
            for t in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(t)
    return len(types)


card = PokemonCardDef(
    guid="1b59be4a-942e-5ada-b337-23941a77fce0",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Conversion Powder",
            game_text="Choose either Asleep or Poisoned. Your opponent's Active Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            effect=_conversion_powder,
        ),
        Attack(
            title="Colorful Wind",
            game_text="This attack does 30 more damage for each different type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(_basic_energy_types_count, 30, base=30),
        ),
    ],
)