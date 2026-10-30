"""STUB: effect not implemented — do not guess mechanics.
Gardevoir (DP3 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="61d1abe2-770b-510e-a426-8f36f38207dc",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Telepass",
            game_text="Once during your turn (before your attack), you may search your opponent's discard pile for a Supporter card and use the effect of that card as the effect of this power. (The Supporter card remains in your opponent's discard pile.) You can't use more than 1 Telepass Pok\u00e9-Power each turn. This power can't be used if Gardevoir is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Lock",
            game_text="During your opponent's next turn, your opponent can't use any Pok\u00e9-Powers on his or her Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)