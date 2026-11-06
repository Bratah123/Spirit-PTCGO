from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import smelly_gas


card = PokemonCardDef(
    guid="6ea25612-b132-59d1-9410-1af442e86ee4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKoffing.Name",
    display_name="Koga's Koffing",
    searchable_by=["Koga's Koffing", "Basic", "KogasKoffing"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Smelly Gas",
            game_text="Flip a coin. If heads, this attack does 10 damage to each Benched Pok\u00e9mon (including your own). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=smelly_gas,
        ),
    ],
)
