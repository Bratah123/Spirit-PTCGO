"""STUB: effect not implemented — do not guess mechanics.
Magnezone (DPP #DP32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69321c77-50da-5891-8e97-bbaba0b773ce",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=462,
    abilities=[
        Attack(
            title="Mirror Shot",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Magnet Slash",
            game_text="Discard all Lightning Energy attached to Magnezone.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)