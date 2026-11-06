from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ember(ctx):
    """Flip a coin. If tails, discard an Energy from this Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Ember"))[0]
    if not heads:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy attached to this Pokémon",
        )


card = PokemonCardDef(
    guid="e57eb906-c932-56a0-9afb-20e29fab5d8a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ember,
        ),
    ],
)