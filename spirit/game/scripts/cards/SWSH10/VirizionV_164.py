from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.models.board import BoardState


def _grass_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.GRASS.value)
               for e in BoardState.attached_energies(target))


async def verdant_wind(ctx):
    """Cures Special Conditions the moment one of your Pokemon picks up
    Grass Energy; the passive keeps it immune from then on."""
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return
    if not energy_provides_type(ctx.attached_energy, PokemonTypes.GRASS.value):
        return
    await ctx.cure_all_conditions(receiver)


async def emerald_blade(ctx):
    """200 damage. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e06f7936-d07c-565d-ae63-5967b6ba2380",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionV.Name",
    display_name="Virizion V",
    searchable_by=["Virizion V", "Basic", "V", "VirizionV"],
    subtypes=["Basic", "V"],
    collector_number=164,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=verdant_wind,
            passive=condition_immunity_passive(protects=_grass_energy_immune),
        ),
        Attack(
            title="Emerald Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=emerald_blade,
        ),
    ],
)