from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def _torment(ctx):
    """Printed damage. Choose 1 of the Defending Pokemon's attacks; it can't
    use that attack during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
               if isinstance(e, dict) and e.get("abilityType") == "Attack" and e.get("abilityID")]
    if not entries:
        return
    index = 0
    if len(entries) > 1:
        index = await ctx.choose("Choose an attack to lock",
                                 [e.get("title", {}).get("id", "Attack") for e in entries])
    state = ctx.session.turn_state
    state.attack_locks[(defender.entity_id, entries[index]["abilityID"])] = state.turn_number + 1


card = PokemonCardDef(
    guid="6516ec40-c7af-5248-8bd7-ab7f0fe47933",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Team Plasma", "Infernape"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=17,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attack. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_torment,
        ),
        Attack(
            title="Malevolent Fire",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)