"""STUB: effect not implemented — do not guess mechanics.
Spiritomb (DP6 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="148f8b56-db87-5d6d-b1dd-1c729cf0b8b7",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=442,
    abilities=[
        Ability(
            title="Curse Breath",
            game_text="Once during your turn, when you put Spiritomb from your hand onto your Bench, you may put 1 damage counter on all Pok\u00e9mon that already have any damage counters on them (both yours and your opponent's). You can't use more than 1 Curse Breath Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Transfer Pain",
            game_text="Move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)