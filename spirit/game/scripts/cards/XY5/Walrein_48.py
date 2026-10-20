from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


async def _knock_over(ctx):
    """50; you may discard any Stadium card in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


def _is_fighting(pokemon):
    return PokemonTypes.FIGHTING.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="10e4a00a-9da2-568d-8e31-32e726ea148a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_knock_over,
        ),
        Attack(
            title="Frozen Splash",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 70 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and _is_fighting(ctx.defender), 70),
        ),
    ],
)