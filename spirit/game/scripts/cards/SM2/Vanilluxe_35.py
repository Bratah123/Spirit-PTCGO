from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.attributes import PokemonTypes


from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.attributes import SpecialConditions


async def frozen_breath(ctx):
    """80 damage; you may discard 2 Water Energy to Paralyze."""
    await ctx.deal_damage()
    waters = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.WATER.value)
    ]
    if len(waters) < 2:
        return
    picks = await ctx.choose_cards(
        waters, 2, minimum=0,
        prompt="You may discard 2 Water Energy to Paralyze",
    )
    if len(picks) == 2:
        await ctx.discard_cards(picks)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="8184ddae-4d9d-5991-a90f-3e4632a2e260",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Hail",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=damage_all_opponents(20),
        ),
        Attack(
            title="Frozen Breath",
            game_text="You may discard 2 Water Energy from this Pok\u00e9mon. If you do, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=frozen_breath,
        ),
    ],
)