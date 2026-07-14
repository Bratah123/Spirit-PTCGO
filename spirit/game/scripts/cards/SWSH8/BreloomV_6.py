from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def counter(ctx):
    """20, plus that much more damage if this Pokémon was damaged by an attack during the opponent's last turn."""
    bonus = ctx.damage_taken_last_turn(ctx.attacker)
    await ctx.deal_damage(20 + bonus)


card = PokemonCardDef(
    guid="987c6de5-d7c3-58af-9d18-be118960ada4",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BreloomV.Name",
    display_name="Breloom V",
    searchable_by=["Breloom V", "Basic", "V", "Single Strike", "BreloomV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=6,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=286,
    abilities=[
        Attack(
            title="Counter",
            game_text="If this Pokémon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=counter,
        ),
        Attack(
            title="Mach Cross",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
