"""STUB: effect not implemented — do not guess mechanics.
Politoed ex (EX10 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import upward_lick, punch_and_run, swallow_up_instead

card = PokemonCardDef(
    guid="9ee40210-93f7-5db7-9500-48e761807025",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoedex.Name",
    display_name="Politoed ex",
    searchable_by=["Politoed ex", "Stage 2", "ex", "Politoedex"],
    subtypes=["Stage 2", "ex"],
    collector_number=107,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Upward Lick",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. If that Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, this attack does 50 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=upward_lick(30, 50),
        ),
        Attack(
            title="Punch and Run",
            game_text="Switch Politoed ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=punch_and_run(),
        ),
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Politoed ex. If the Defending Pok\u00e9mon has fewer remaining HP than Politoed ex's, this attack does 120 damage instead.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=swallow_up_instead(70, 120),
        ),
    ],
)