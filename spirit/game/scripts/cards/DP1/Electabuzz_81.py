"""STUB: effect not implemented — do not guess mechanics.
Electabuzz (DP1 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import thunderpunch_recoil
from spirit.game.card_effects.dp import shock_wave_elekid

card = PokemonCardDef(
    guid="cba298aa-cd38-5a74-b3f1-0d65bf837fa9",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=125,
    abilities=[
        Attack(
            title="Thunderpunch",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage. If tails, Electabuzz does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=thunderpunch_recoil(),
        ),
        Attack(
            title="Shock Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If Electabuzz is evolved from Elekid, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=shock_wave_elekid(),
        ),
    ],
)