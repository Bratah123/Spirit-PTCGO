from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def _scout(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = PokemonCardDef(
    guid="ec0d792a-3173-545e-a062-eb7c2f738676",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Clairvoyance",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_scout,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=40),
        ),
    ],
)