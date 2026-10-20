from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _non_grass(p):
    return p is not None and PokemonTypes.GRASS.value not in (p.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _poisonous_nest(ctx):
    """Both Active Pokemon (except Grass Pokemon) are now Poisoned."""
    for p in (ctx.my_active(), ctx.opponent_active()):
        if _non_grass(p):
            await ctx.apply_special_condition(p, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="4a3719c7-9265-586e-990a-b2fde450ba05",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Poisonous Nest",
            game_text="Once during your turn (before your attack), you may use this Ability. Both Active Pok\u00e9mon (except for Grass Pok\u00e9mon) are now Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            effect=_poisonous_nest,
        ),
        Attack(
            title="Impound",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)