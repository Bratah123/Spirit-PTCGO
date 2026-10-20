from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card


def _basic_fire(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _savage_wing(ctx):
    """100+; discard any number of basic Fire Energy from this Pokemon: +40 each."""
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _basic_fire(e)]
    picks = []
    if pool:
        picks = list(await ctx.choose_cards(pool, len(pool), minimum=0,
                                            prompt="Choose basic Fire Energy to discard") or [])
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(ctx.ability.damage + 40 * len(picks))


card = PokemonCardDef(
    guid="c948a6c5-4052-5a6a-8b58-c9968bf2f5bb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSalamenceEX.Name",
    display_name="M Salamence-EX",
    searchable_by=["M Salamence-EX", "MEGA", "EX", "MSalamenceEX"],
    subtypes=["MEGA", "EX"],
    collector_number=171,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceEX.Name",
    family_id=373,
    abilities=[
        Attack(
            title="Savage Wing",
            game_text="Discard as many basic Fire Energy attached to this Pok\u00e9mon as you like. This attack does 40 more damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=_savage_wing,
        ),
    ],
)