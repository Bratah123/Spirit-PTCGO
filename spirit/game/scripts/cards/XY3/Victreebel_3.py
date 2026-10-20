from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _wafting_condition(board, player_id, pokemon=None):
    return pokemon is not None and any(_is_grass_energy(c) for c in pokemon.children)


async def _wafting_scent(ctx):
    """Discard a Grass Energy from this Pokemon: the opponent's Active is now
    Confused and Poisoned."""
    discarded = await ctx.discard_energy_from(ctx.source, 1, predicate=_is_grass_energy,
                                              minimum=1, prompt="Discard a Grass Energy")
    target = ctx.opponent_active()
    if discarded and target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)
        await ctx.apply_special_condition(target, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="24820a9f-2949-5d5b-b7a1-c9662278bd00",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Wafting Scent",
            game_text="Once during your turn (before your attack), you may discard a Grass Energy attached to this Pok\u00e9mon. If you do, your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_wafting_condition,
            effect=_wafting_scent,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=heal_attack(30),
        ),
    ],
)