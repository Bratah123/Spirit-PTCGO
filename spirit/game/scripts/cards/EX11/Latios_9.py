"""STUB: effect not implemented — do not guess mechanics.
Latios δ (EX11 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_aura_cost_passive
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e699d246-7f47-5b1d-98d6-dc3890e83e16",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios δ",
    searchable_by=["Latios \u03b4", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Ability(
            title="Delta Aura",
            game_text="If you have Latias or Latias ex in play, the attack cost of Latios's Psychic Force is now Lightning MetalColorless.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=delta_aura_cost_passive('Latias', attack_title='Psychic Force'),
            effect=None,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Psychic Force",
            game_text="If your opponent has no Stage 2 Evolved Pok\u00e9mon in play, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=None,
        ),
    ],
)