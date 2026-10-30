"""STUB: effect not implemented — do not guess mechanics.
Dodrio (EX5 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import fast_feet_passive, retaliate_damage, slashing_strike_lock

card = PokemonCardDef(
    guid="c5f09740-2edb-551e-a5e7-4afeb49cf3d6",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Fast Feet",
            game_text="Dodrio can retreat even when it is Asleep or Paralyzed.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=fast_feet_passive(),
        ),
        Attack(
            title="Retaliate",
            game_text="Does 10 damage times the number of damage counters on Dodrio.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=retaliate_damage(),
        ),
        Attack(
            title="Slashing Strike",
            game_text="Flip a coin. If tails, Dodrio can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=slashing_strike_lock(),
        ),
    ],
)