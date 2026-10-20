from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ember(ctx):
    """20 damage. Flip a coin. If tails, discard an Energy from this Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Ember"))[0]
    if not heads:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy attached to this Pokémon",
        )


card = PokemonCardDef(
    guid="1aed4883-5b9d-5891-b80a-c6c609e2a155",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Flamethrower",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ember,
        ),
    ],
)