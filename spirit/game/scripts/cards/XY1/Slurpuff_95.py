from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.models.board import BoardState


async def _sweet_veil(ctx):
    """Cures Special Conditions the moment one of your Pokemon picks up Fairy
    Energy; the passive keeps it immune from then on."""
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return
    if not energy_provides_type(ctx.attached_energy, PokemonTypes.FAIRY.value):
        return
    await ctx.cure_all_conditions(receiver)


def _fairy_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.FAIRY.value)
               for e in BoardState.attached_energies(target))


card = PokemonCardDef(
    guid="f891eabf-094e-5418-9f15-16735bcc9c9c",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Ability(
            title="Sweet Veil",
            game_text="Each of your Pok\u00e9mon that has any Fairy Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_sweet_veil,
            passive=condition_immunity_passive(protects=_fairy_energy_immune),
        ),
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
    ],
)