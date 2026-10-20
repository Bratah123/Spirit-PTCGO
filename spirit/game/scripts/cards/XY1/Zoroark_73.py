from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def _fire_spin(ctx):
    """Printed damage. Flip a coin. If tails, discard 2 Energy from this Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Fire Spin")
    if results and not results[0]:
        await ctx.discard_energy_from(ctx.attacker, 2)


card = PokemonCardDef(
    guid="288f0410-9b74-5d31-847f-72d1fcb3dd7c",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Night Claw",
            game_text="Flip a coin. If tails, discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=_fire_spin,
        ),
    ],
)