from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _giga_drain(ctx):
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)


card = PokemonCardDef(
    guid="e2234c68-8d01-5d4a-a8da-7863c5b7036f",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Shadow Drain",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_giga_drain,
        ),
        Attack(
            title="Slashing Strike",
            game_text="This Pok\u00e9mon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)