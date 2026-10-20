from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.pokemon import is_energy_card


async def psy_report(ctx):
    """Printed damage; your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)


def _energized_ally(target, carrier):
    return target.owning_player_id == carrier.owning_player_id and \
        any(is_energy_card(c) for c in target.children)


card = PokemonCardDef(
    guid="26a381e3-9445-5ae4-96da-9e93456ff86f",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Solar Revelation",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon that has any Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=attack_effect_shield_passive(protects=_energized_ally),
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=psy_report,
        ),
    ],
)