from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.content.definitions import def_for


def _escavalier_kod_last_turn(ctx):
    ledger = ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, [])
    return any(getattr(def_for(e.get("archetype_id")), "display_name", "") == "Escavalier"
               for e in ledger)


async def _retribution(ctx):
    """Printed damage; if an Escavalier you had in play was Knocked Out by
    damage from an opponent's attack during their last turn, put all Energy
    attached to the Defending Pokemon into your opponent's hand."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is None or ctx.effects_blocked(d) or not _escavalier_kod_last_turn(ctx):
        return
    energies = ctx.attached_energies(d)
    if energies:
        await ctx.put_in_hand(energies, reveal=False)


card = PokemonCardDef(
    guid="f9e60143-4b3d-5115-a3e1-902682216b4a",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Team Plasma", "Accelgor"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=8,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Retribution",
            game_text="If an Escavalier you had in play was Knocked Out by damage from an opponent's attack during his or her last turn, put all Energy attached to the Defending Pok\u00e9mon into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_retribution,
        ),
        Attack(
            title="Signal Beam",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)