from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _draining_cut(ctx):
    """Flip 2 coins: 40x heads; heal this Pokémon by the damage done."""
    results = await ctx.flip_coins(2, "Draining Cut")
    heads = sum(1 for r in results if r)
    if not heads:
        return
    dealt = await ctx.deal_damage(40 * heads)
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


card = PokemonCardDef(
    guid="d649b036-77f2-566e-8dc4-8e6ff4a92ce0",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name",
    display_name="Kricketune",
    searchable_by=["Kricketune", "Stage 1", "Kricketune"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    family_id=401,
    abilities=[
        Attack(
            title="White Noise",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Draining Cut",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads. Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=_draining_cut,
        ),
    ],
)