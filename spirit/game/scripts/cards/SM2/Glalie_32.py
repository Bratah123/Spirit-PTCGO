from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def cut_down(ctx):
    """Printed damage; flip a coin, heads: discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Crunch")
    if not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy to discard from the Defending Pokémon.",
    )


card = PokemonCardDef(
    guid="46d4d965-63c3-54b1-a6e6-4634119c96e4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=cut_down,
        ),
        Attack(
            title="Raging Floe",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 3},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(has_damage('self'), 80),
        ),
    ],
)