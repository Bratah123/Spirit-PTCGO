from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _scout(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = PokemonCardDef(
    guid="11b1d21d-ea72-5807-95fe-fc6fb5f36654",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=519,
    abilities=[
        Attack(
            title="Scout",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_scout,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)