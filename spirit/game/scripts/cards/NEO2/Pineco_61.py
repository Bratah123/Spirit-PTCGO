from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import pineco_burst


card = PokemonCardDef(
    guid="56b529b4-a678-5df2-8877-21666f74e9ff",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic", "Pineco"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Burst",
            game_text="Flip a coin. If heads, Pineco does 40 damage to itself and 10 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Flip a coin. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=pineco_burst,
        ),
    ],
)
