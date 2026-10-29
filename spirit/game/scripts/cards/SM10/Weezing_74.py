from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    detention_gas,
    splattering_sludge,
)

card = PokemonCardDef(
    guid="b2282a57-9921-59b8-a03a-13ef30e29e20",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Detention Gas",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Basic Pok\u00e9mon between turns.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=detention_gas
        ),
        Attack(
            title="Splattering Sludge",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=splattering_sludge
        ),
    ],
)