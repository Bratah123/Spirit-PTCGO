from spirit.game.card_effects.ex import froth_on_evolve, water_punch
"""STUB: effect not implemented — do not guess mechanics.
Azumarill (EX7 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fe5c7ed5-4e87-5a47-9364-2b165b259bb3",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Froth",
            game_text="Once during your turn, when you play Azumarill from your hand to evolve 1 of your Active Pok\u00e9mon, you may use this power. Each Defending Pok\u00e9mon is now Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=froth_on_evolve(),
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a coin for each Water Energy attached to Azumarill. This attack does 20 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=water_punch(),
        ),
    ],
)