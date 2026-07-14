from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def silence(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks; it can't be used
    during their next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
               if isinstance(e, dict) and e.get("abilityType") == "Attack"
               and e.get("abilityID")]
    if not entries:
        return
    titles = [e.get("title", {}).get("id", "Attack") for e in entries]
    idx = await ctx.choose("Choose an attack to Silence", titles)
    entry = entries[idx]
    ctx.session.turn_state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
        ctx.session.turn_state.turn_number + 1


card = PokemonCardDef(
    guid="b651cb52-3dac-5464-9504-ecf2a75e8ebd",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=161,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Silence",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. During your opponent's next turn, that Pok\u00e9mon can't use that attack.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=silence,
        ),
        Attack(
            title="Merciless Strike",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 90),
        ),
    ],
)