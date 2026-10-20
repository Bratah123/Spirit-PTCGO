from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import smokescreen_attack


def _is_fairy(pokemon):
    return PokemonTypes.FAIRY.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _diamond_storm(ctx):
    """60; heal 30 damage from each of your Fairy Pokemon."""
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        if _is_fairy(p):
            await ctx.heal(30, p)


card = PokemonCardDef(
    guid="96ad0e44-d289-5b19-b6fa-b46fd79834e1",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Attack(
            title="Sparkle",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FAIRY: 1},
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Diamond Storm",
            game_text="Heal 30 damage from each of your Fairy Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=_diamond_storm,
        ),
    ],
)