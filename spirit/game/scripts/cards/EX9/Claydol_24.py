"""STUB: effect not implemented — do not guess mechanics.
Claydol (EX9 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import levitate_any_energy_passive


card = PokemonCardDef(
    guid="89e119e2-68f1-5033-b68c-1af2b597a48a",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Levitate",
            game_text="As long as Claydol has any Energy attached to it, the Retreat Cost for Claydol is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=levitate_any_energy_passive(),
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)