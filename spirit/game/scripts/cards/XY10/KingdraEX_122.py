from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _gaia_crush(ctx):
    """Printed damage; discard any Stadium card in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _dragon_trail(ctx):
    """60+; 30 more per basic Lightning Energy attached to this Pokemon."""
    n = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e) and _is_lightning_energy(e))
    await ctx.deal_damage(ctx.ability.damage + 30 * n)


card = PokemonCardDef(
    guid="c8d0af95-dc7e-5b2a-9516-5a21ebe4d585",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KingdraEX.Name",
    display_name="Kingdra-EX",
    searchable_by=["Kingdra-EX", "Basic", "EX", "KingdraEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=230,
    abilities=[
        Attack(
            title="Big Storm",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_gaia_crush,
        ),
        Attack(
            title="Dragon Trail",
            game_text="This attack does 30 more damage for each basic Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=_dragon_trail,
        ),
    ],
)