"""STUB: effect not implemented — do not guess mechanics.
Aggron (EX16 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import mill_opponent_top, terraforming_look5


card = PokemonCardDef(
    guid="09adcbe2-1041-56b1-84fa-8ca3e920e647",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Ability(
            title="Terraforming",
            game_text="Once during your turn (before your attack), you may look at the top 5 cards from your deck and put them back on top of your deck in any order. This power can't be used if Aggron is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=terraforming_look5(),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Mix-Up",
            game_text="Your opponent discards the top card of his or her deck.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=mill_opponent_top(1),
        ),
    ],
)