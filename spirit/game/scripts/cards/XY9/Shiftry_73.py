"""STUB: effect not implemented — do not guess mechanics.
Shiftry (XY9 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import electromagnetic_sonar


card = PokemonCardDef(
    guid="6e5b96c8-b6a0-55de-a1f6-bf9cfcb1c659",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Roll Up",
            game_text="Flip 3 coins. If any of them are heads, your opponent reveals his or her hand. Then, for each heads, discard a card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Otherworldly Return",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=electromagnetic_sonar,
        ),
    ],
)