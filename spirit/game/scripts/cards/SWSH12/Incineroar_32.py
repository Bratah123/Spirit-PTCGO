from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, def_for, evolves_from_chain,
)
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.effects import full_stack, is_pokemon_card


def _logic_name(definition):
    spec = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    return spec.get("value") if isinstance(spec, dict) else None


async def secret_attack(ctx):
    """Choose an attack from 1 of this Pokémon's previous Evolutions and use it as this attack."""
    names = set(evolves_from_chain(ctx.attacker.archetype_id))
    candidates = []
    if names:
        for card in full_stack(ctx.attacker)[1:]:
            if not is_pokemon_card(card):
                continue
            definition = def_for(card.archetype_id)
            if definition is None or _logic_name(definition) not in names:
                continue
            for ability in getattr(definition, "abilities", []):
                if isinstance(ability, Attack):
                    candidates.append((card, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
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
    guid="f959df23-74b4-575f-a3c4-ad53b717a10d",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name",
    display_name="Incineroar",
    searchable_by=["Incineroar", "Stage 2", "Incineroar"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Secret Attack",
            game_text="Choose an attack from 1 of this Pok\u00e9mon's previous Evolutions and use it as this attack.",
            cost={PokemonTypes.FIRE: 1},
            effect=secret_attack,
        ),
        Attack(
            title="Flare Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)