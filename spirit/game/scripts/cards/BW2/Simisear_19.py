from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import energy_provides_type


async def waters_power(ctx):
    """30. If this Pokémon has any Water Energy, Defending is Asleep."""
    await ctx.deal_damage()
    if any(
        energy_provides_type(e, PokemonTypes.WATER.value)
        for e in ctx.attached_energies(ctx.attacker)
    ):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="a43a4430-61a8-5729-8ce5-176ffcff086e",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Water's Power",
            game_text="If this Pok\u00e9mon has any Water Energy attached to it, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=waters_power,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
