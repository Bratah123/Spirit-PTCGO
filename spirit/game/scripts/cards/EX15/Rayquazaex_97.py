"""STUB: effect not implemented — do not guess mechanics.
Rayquaza ex δ (EX15 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import rage_aura_ignore_colorless, special_circuit
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="459957cb-e9aa-5025-8c91-630d9b51819d",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquazaex.Name",
    display_name="Rayquaza ex δ",
    searchable_by=["Rayquaza ex \u03b4", "Basic", "ex", "Rayquazaex"],
    subtypes=["Basic", "ex"],
    collector_number=97,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=384,
    abilities=[
        Ability(
            title="Rage Aura",
            game_text="If you have more Prize cards left than your opponent, ignore all Colorless Energy necessary to use Rayquaza ex's Special Circuit and Sky-high Claws attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=rage_aura_ignore_colorless(),
        ),
        Attack(
            title="Special Circuit",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to the Pok\u00e9mon. If you choose a Pok\u00e9mon that has any Pok\u00e9-Powers or Pok\u00e9-Bodies, this attack does 50 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=special_circuit(30, 50),
        ),
        Attack(
            title="Sky-high Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)