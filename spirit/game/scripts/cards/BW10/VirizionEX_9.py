from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.models.board import BoardState


async def verdant_wind(ctx):
    """Cures Special Conditions the moment one of your Pokemon picks up
    Grass Energy; the passive keeps it immune from then on."""
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return
    if not energy_provides_type(ctx.attached_energy, PokemonTypes.GRASS.value):
        return
    await ctx.cure_all_conditions(receiver)


def _grass_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.GRASS.value)
               for e in BoardState.attached_energies(target))


card = PokemonCardDef(
    guid="d0122962-d935-5e0d-a9de-3ae8b0465185",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionEX.Name",
    display_name="Virizion-EX",
    searchable_by=["Virizion-EX", "Basic", "EX", "VirizionEX"],
    subtypes=["Basic", "EX"],
    collector_number=9,
    set_code="BW10",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=verdant_wind,
            passive=condition_immunity_passive(protects=_grass_energy_immune),
        ),
        Attack(
            title="Emerald Slash",
            game_text="You may search your deck for 2 Grass Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)