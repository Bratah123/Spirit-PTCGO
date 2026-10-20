from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.trainers import is_energy_card


def _gooey_condition(board, player_id, pokemon=None):
    return pokemon is not None and any(is_energy_card(c) for c in pokemon.children)


async def _gooey_regeneration(ctx):
    """Discard an Energy attached to this Pokemon. If you do, heal 60 damage from it."""
    discarded = await ctx.discard_energy_from(ctx.source, 1, minimum=1,
                                              prompt="Choose an Energy to discard")
    if discarded:
        await ctx.heal(60, ctx.source)


card = PokemonCardDef(
    guid="e99c4014-b252-55c3-807f-98d71c354c2d",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Gooey Regeneration",
            game_text="As often as you like during your turn (before your attack), you may discard an Energy attached to this Pok\u00e9mon. If you do, heal 60 damage from this Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_gooey_condition,
            effect=_gooey_regeneration,
        ),
        Attack(
            title="Heavy Whip",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)