"""STUB: effect not implemented — do not guess mechanics.
Golbat (XY4 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


card = PokemonCardDef(
    guid="ee69ea01-4ea5-5f12-a37a-2bd95aea1031",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1", "Golbat"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Sneaky Bite",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Swoop Across",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(10),
        ),
    ],
)