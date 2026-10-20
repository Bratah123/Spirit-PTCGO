from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _goodnight_babies(ctx):
    """Leave both Active Pokemon Asleep."""
    for p in (ctx.my_active(), ctx.opponent_active()):
        if p is not None:
            await ctx.apply_special_condition(p, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="326f178e-93e8-5403-bcd0-778cc7c1e51e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Goodnight, Babies",
            game_text="Once during your turn (before your attack), you may leave both Active Pok\u00e9mon Asleep.",
            activation=Activations.ONCE_PER_TURN,
            effect=_goodnight_babies,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)