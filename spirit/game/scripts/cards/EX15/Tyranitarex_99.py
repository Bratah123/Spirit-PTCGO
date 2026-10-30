"""STUB: effect not implemented — do not guess mechanics.
Tyranitar ex δ (EX15 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import electromark, hyper_claws_vs_stage2, shock_wave_ko_marked
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe3a4081-15f4-507f-a327-35fbdbb3af0a",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex δ",
    searchable_by=["Tyranitar ex \u03b4", "Stage 2", "ex", "Tyranitarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=99,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Electromark",
            game_text="Put a Shock-wave marker on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=electromark(),
        ),
        Attack(
            title="Hyper Claws",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, this attack does 70 damage plus 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hyper_claws_vs_stage2(70, 20),
        ),
        Attack(
            title="Shock-wave",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any Shock-wave markers on it. That Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=shock_wave_ko_marked(),
        ),
    ],
)