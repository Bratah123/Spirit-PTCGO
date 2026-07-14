from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import gust_then


async def _alluring_dance_confuse(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="3747552a-4458-5823-a691-604aecc92702",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=124,
    abilities=[
        Attack(
            title="Alluring Dance",
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=gust_then(_alluring_dance_confuse),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
