from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for, evolves_from_chain
from spirit.game.attributes import AttrID
from spirit.game.session.effects import full_stack, is_pokemon_card
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


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


def _logic_name(definition):
    spec = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    return spec.get("value") if isinstance(spec, dict) else None


card = PokemonCardDef(
    guid="21daeca1-d526-59f7-b896-8a77e92444b0",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Recall",
            game_text="Choose an attack from 1 of this Pok\u00e9mon's previous Evolutions and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=secret_attack,
        ),
        Attack(
            title="Aquafall",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)