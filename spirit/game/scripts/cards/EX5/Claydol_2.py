"""STUB: effect not implemented — do not guess mechanics.
Claydol (EX5 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import muddy_eye, primal_pull_passive

card = PokemonCardDef(
    guid="5d176eba-f967-576c-9ab3-11c95959991f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Primal Pull",
            game_text="As long as Claydol is your Active Pok\u00e9mon, each player's Evolved Pok\u00e9mon pays Colorless more Energy to use its attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=primal_pull_passive(),
        ),
        Attack(
            title="Muddy Eye",
            game_text="Does 10 damage times the number of basic Energy cards attached to Claydol and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=muddy_eye(),
        ),
    ],
)