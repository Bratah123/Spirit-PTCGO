"""STUB: effect not implemented — do not guess mechanics.
Wormadam Sandy Cloak (DP3 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="aaacca67-9dc9-55dc-b77a-be6719227e8d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamSandyCloak.Name",
    display_name="Wormadam Sandy Cloak",
    searchable_by=["Wormadam Sandy Cloak", "Stage 1", "WormadamSandyCloak"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Sandy Cloak",
            game_text="Prevent all effects of attacks, excluding damage, done to Wormadam Sandy Cloak.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Push Over",
            game_text="Does 40 damage plus 10 damage for each Fighting Energy attached to Wormadam Sandy Cloak.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)