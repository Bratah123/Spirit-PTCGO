from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import def_for
from spirit.game.card_effects.sm7 import (
    deck_has_cards,
    excavate,
)
from spirit.game.data_utils import Activations


async def amnesia(ctx):
    """20 damage; lock 1 of the Defending Pokémon's attacks next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", []) or []
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to lock")
    if picked is None:
        return
    _, chosen = picked
    ctx.session.turn_state.lock_attack(defender.entity_id, chosen.ability_id)


card = PokemonCardDef(
    guid="3d0d3dcf-26c8-506e-9d89-a70a672c10ed",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Ability(
            title="Excavate",
            game_text="Once during your turn (before your attack), you may look at the top card of your deck. You may discard that card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=excavate,
            condition=deck_has_cards,
        ),
        Attack(
            title="Disable",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
    ],
)