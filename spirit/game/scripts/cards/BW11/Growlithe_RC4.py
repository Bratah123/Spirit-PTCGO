from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def _rest(ctx):
    """Heal all damage from this Pokemon. This Pokemon is now Asleep."""
    me = ctx.attacker
    await ctx.heal(ctx.max_hp(me), me)
    await ctx.apply_special_condition(me, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="f2a4375e-32ee-5f50-8341-1cdc3077d062",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Rest",
            game_text="Heal all damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_rest,
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)