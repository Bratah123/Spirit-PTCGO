"""STUB: effect not implemented — do not guess mechanics.
Empoleon (DP7 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp3_vibrava_74_hyper_beam


card = PokemonCardDef(
    guid="e739f37e-a495-568a-9ba2-04a6adbc0982",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Ability(
            title="Emperor Aura",
            game_text="Once during your turn (before your attack), when you play Empoleon from your hand to evolve 1 of your Active Pok\u00e9mon, you may use this power. Your opponent can't attach any Energy cards from his or her hand to his or her Pok\u00e9mon during your opponent's next turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to Empoleon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=dp3_vibrava_74_hyper_beam(),
        ),
    ],
)