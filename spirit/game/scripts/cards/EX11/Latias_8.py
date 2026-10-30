"""STUB: effect not implemented — do not guess mechanics.
Latias δ (EX11 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_aura_cost_passive, extra_crush_requires_ex, spiral_drain_heal
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="69c3b9c9-1986-54b1-9f71-592d3cb45932",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias δ",
    searchable_by=["Latias \u03b4", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Delta Aura",
            game_text="If you have Latios or Latios ex in play, the attack cost of Latias's Extra Crush is now Lightning MetalColorless.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=delta_aura_cost_passive('Latios', attack_title='Extra Crush'),
            effect=None,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters fro Latias.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spiral_drain_heal(2),
        ),
        Attack(
            title="Extra Crush",
            game_text="If your opponent has no Pok\u00e9mon-ex in play, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=extra_crush_requires_ex(80),
        ),
    ],
)