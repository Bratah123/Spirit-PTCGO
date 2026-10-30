"""STUB: effect not implemented — do not guess mechanics.
Poliwrath (EX10 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import spiral_swirl_on_ko_passive, beatdown_vs_dark, hyper_splash

card = PokemonCardDef(
    guid="956db333-5eed-5ca8-a933-39fe5c8a1059",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Spiral Swirl",
            game_text="If Poliwrath is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, the Attacking Pok\u00e9mon is now Confused.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=spiral_swirl_on_ko_passive(),
        ),
        Attack(
            title="Beatdown",
            game_text="If the Defending Pok\u00e9mon is a Darkness Pok\u00e9mon or has Dark in its name, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=beatdown_vs_dark(40, 30),
        ),
        Attack(
            title="Hyper Splash",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, this attack does 60 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hyper_splash(60, 30),
        ),
    ],
)