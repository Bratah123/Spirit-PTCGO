"""STUB: effect not implemented — do not guess mechanics.
Vespiquen (DP7 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="eb8e0fab-f1b5-51f5-8e00-282bcc8a1148",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Ability(
            title="Green Dignity",
            game_text="As long as you have more Prize cards left than your opponent, Vespiquen's attacks do 10 more damage for each Grass Pok\u00e9mon on your Bench to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bee Drain",
            game_text="After your attack, remove from Vespiquen the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bee Powder",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Burned, Paralyzed, and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)