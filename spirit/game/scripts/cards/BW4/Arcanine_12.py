from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.pokemon import in_active_spot


async def _fire_spin(ctx):
    """Printed damage. Flip a coin. If tails, discard 2 Energy from this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Fire Spin")
    if results and not results[0]:
        await ctx.discard_energy_from(ctx.attacker, 2)


async def _blazing_mane(ctx):
    """Active only: the Attacking Pokémon is now Burned."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="f04248f7-a04a-5720-bfba-cc97dbb50df4",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Blazing Mane",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_blazing_mane,
        ),
        Attack(
            title="Fire Spin",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_fire_spin,
        ),
    ],
)