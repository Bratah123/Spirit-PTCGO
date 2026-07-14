from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def grass_munch(ctx):
    """10 damage, then discard a Grass Energy from the opponent's Active."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1, predicate=lambda c: energy_provides_type(c, PokemonTypes.GRASS.value),
        prompt="Choose a Grass Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="815eebbc-d71a-53a9-bc69-78595e5d0082",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    display_name="Sewaddle",
    searchable_by=["Sewaddle", "Basic", "Sewaddle"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=540,
    abilities=[
        Attack(
            title="Grass Munch",
            game_text="Discard a Grass Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=grass_munch,
        ),
    ],
)