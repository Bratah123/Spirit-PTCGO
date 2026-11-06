from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.content.definitions import def_for


async def _phantom_gate(ctx):
    """Choose 1 of your opponent's Pokemon's attacks and use it as this attack."""
    candidates = [(p, a) for p in ctx.opponent_pokemon_in_play()
                  for a in getattr(def_for(p.archetype_id), "abilities", []) or []
                  if isinstance(a, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, entry["abilityID"])


card = PokemonCardDef(
    guid="81202dc4-d550-5d47-9c6d-47688020b93f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGengarEX.Name",
    display_name="M Gengar-EX",
    searchable_by=["M Gengar-EX", "MEGA", "EX", "MGengarEX"],
    subtypes=["MEGA", "EX"],
    collector_number=35,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name",
    family_id=94,
    abilities=[
        Attack(
            title="Phantom Gate",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=_phantom_gate,
        ),
    ],
)