from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.attacks_common import damage_counters_on


async def karate_chop(ctx):
    """60 minus 10 per damage counter on this Pokémon."""
    amount = max(0, 60 - 10 * damage_counters_on()(ctx))
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="9e9a0d3a-69a9-5740-9bc4-092a722a693e",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Karate Chop",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="-",
            effect=karate_chop,
        ),
    ],
)