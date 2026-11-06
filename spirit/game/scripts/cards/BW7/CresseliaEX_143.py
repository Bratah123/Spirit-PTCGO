from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import no_weakness_passive


async def _cavalry_lance(ctx):
    """Printed damage; during your opponent's next turn this Pokémon has no Weakness."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, no_weakness_passive())


async def _sparkling_particles(ctx):
    """At any time between turns, heal 10 damage from this Pokemon."""
    await ctx.heal(10, ctx.source)


card = PokemonCardDef(
    guid="2d14885c-a6db-55b6-8a63-0742c340ca2d",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CresseliaEX.Name",
    display_name="Cresselia-EX",
    searchable_by=["Cresselia-EX", "Basic", "EX", "CresseliaEX"],
    subtypes=["Basic", "EX"],
    collector_number=143,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Ability(
            title="Sparkling Particles",
            game_text="At any time between turns, heal 10 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=_sparkling_particles,
        ),
        Attack(
            title="Psychic Protection",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=_cavalry_lance,
        ),
    ],
)