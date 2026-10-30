"""STUB: effect not implemented — do not guess mechanics.
Latios ★ (EX8 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import miraculous_light_heal_cure, shining_star_vs_stage2


card = PokemonCardDef(
    guid="14aee23b-35f0-5da5-b738-e16c0b3aef1d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios ★",
    searchable_by=["Latios \u2605", "Basic", "Star", "Latios"],
    subtypes=["Basic", "Star"],
    collector_number=106,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Attack(
            title="Miraculous Light",
            game_text="Remove 1 damage counter and all Special Conditions from Latios Star.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=miraculous_light_heal_cure(),
        ),
        Attack(
            title="Shining Star",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, discard all Energy cards attached to Latios Star and this attack does 50 damage plus 100 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=shining_star_vs_stage2(),
        ),
    ],
)