"""STUB: effect not implemented — do not guess mechanics.
Dark Tyranitar (EX7 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import second_strike, sand_damage_between_turns


card = PokemonCardDef(
    guid="f262c760-9a51-5d41-88a6-cdad170307d7",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyranitar.Name",
    display_name="Dark Tyranitar",
    searchable_by=["Dark Tyranitar", "Stage 2", "DarkTyranitar"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Sand Damage",
            trigger=Triggers.BETWEEN_TURNS,
            game_text="As long as Dark Tyranitar is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Benched Basic Pok\u00e9mon between turns. You can't use more than 1 Sand Damage Pok\u00e9-Body between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=sand_damage_between_turns(),
        ),
        Attack(
            title="Second Strike",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=second_strike(50, 20, 2),
        ),
    ],
)