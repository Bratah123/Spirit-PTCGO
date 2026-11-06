from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.attacks_common import snipe_attack


async def _lock_item(ctx):
    """Printed damage; your opponent can't play item cards from their hand during their next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="e72434b2-a0db-5de2-8862-4737551e5936",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SeismitoadEX.Name",
    display_name="Seismitoad-EX",
    searchable_by=["Seismitoad-EX", "Basic", "EX", "SeismitoadEX"],
    subtypes=["Basic", "EX"],
    collector_number=106,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=537,
    abilities=[
        Attack(
            title="Quaking Punch",
            game_text="Your opponent can't play any Item cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_lock_item,
        ),
        Attack(
            title="Grenade Hammer",
            game_text="This attack does 30 damage to 2 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=snipe_attack(30, pool='bench', count=2, also_base=True),
        ),
    ],
)