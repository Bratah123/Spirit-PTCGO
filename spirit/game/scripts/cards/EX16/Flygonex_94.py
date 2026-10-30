"""STUB: effect not implemented — do not guess mechanics.
Flygon ex (EX16 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import psychic_protector_discard_reduce, slashing_strike_lock
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="315b5d78-8cbb-511c-966d-be53013aa8ec",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygonex.Name",
    display_name="Flygon ex",
    searchable_by=["Flygon ex", "Stage 2", "ex", "Flygonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=94,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Psychic Protector",
            game_text="If Flygon ex is damaged by an opponent's attack, you may discard up to 4 cards from your hand. If you do, any damage done to Flygon ex is reduced by 10 for each card you discarded.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=psychic_protector_discard_reduce(),
        ),
        Attack(
            title="Slashing Strike",
            game_text="Flip a coin. If tails, Flygon ex can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=slashing_strike_lock(flip=True),
        ),
    ],
)