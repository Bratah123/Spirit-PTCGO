from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.attacks_common import spread_damage


async def cold_absorption(ctx):
    """Whenever you attach a Water Energy card from your hand to this Pokemon, heal 30 damage from it."""
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    energy = ctx.attached_energy
    if energy is None or not energy_provides_type(energy, PokemonTypes.WATER.value):
        return
    await ctx.heal(30, ctx.source)


card = PokemonCardDef(
    guid="4658ad41-9e37-593f-90ad-96ff2eb7d14d",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EiscueV.Name",
    display_name="Eiscue V",
    searchable_by=["Eiscue V", "Basic", "V", "EiscueV"],
    subtypes=["Basic", "V"],
    collector_number=55,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Ability(
            title="Cold Absorption",
            game_text="Whenever you attach a Water Energy card from your hand to this Pok\u00e9mon during your turn, heal 30 damage from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=cold_absorption,
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=spread_damage(10, side="opponent", also_base=True),
        ),
    ],
)