"""STUB: effect not implemented — do not guess mechanics.
Rayquaza δ (EX11 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_guard_noop_passive, lightning_storm_self, power_blow
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6b3e443d-fc6a-57b0-8b8f-2eaa44240e96",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza δ",
    searchable_by=["Rayquaza \u03b4", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Delta Guard",
            game_text="As long as Rayquaza has any Holon Energy cards attached to it, ignore the effect of Rayquaza's Lightning Storm attack.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=delta_guard_noop_passive(),
            effect=None,
        ),
        Attack(
            title="Power Blow",
            game_text="Does 10 damage times the amount of Energy attached to Rayquaza.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="x",
            effect=power_blow(),
        ),
        Attack(
            title="Lightning Storm",
            game_text="Put 7 damage counters on Rayquaza.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=lightning_storm_self(70, 7),
        ),
    ],
)