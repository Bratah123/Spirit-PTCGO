"""STUB: effect not implemented — do not guess mechanics.
Unown [F] (DP4 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f5647ea8-68c0-589e-a619-6c4363471e84",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownF.Name",
    display_name="Unown [F]",
    searchable_by=["Unown [F]", "Basic", "UnownF"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="FAKE",
            game_text="Once during your turn (before your attack), if Unown F is on your Bench, you may use this power. Put a coin next to your Active Pok\u00e9mon without showing your opponent and cover it with your hand. Your opponent guesses if the coin is heads or tails. If he or she is wrong, draw a card.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="You may flip a coin. If tails, this attack does nothing. If heads, this attack's base damage is 30.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)