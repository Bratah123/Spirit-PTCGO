from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _firefighting(ctx):
    """Printed damage; discard a Fire Energy attached to the Defending Pokemon."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        await ctx.discard_energy_from(d, 1, predicate=_is_fire_energy,
                                      prompt="Choose a Fire Energy to discard")


card = PokemonCardDef(
    guid="b6e34221-da09-5b1d-87ef-6891ab236b10",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Firefighting",
            game_text="Discard a Fire Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=_firefighting,
        ),
    ],
)