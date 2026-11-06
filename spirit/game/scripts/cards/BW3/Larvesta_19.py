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
    guid="17378d78-4b62-5837-be95-6fbc4f79992b",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    display_name="Larvesta",
    searchable_by=["Larvesta", "Basic", "Larvesta"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=636,
    abilities=[
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=ember,
        ),
    ],
)
