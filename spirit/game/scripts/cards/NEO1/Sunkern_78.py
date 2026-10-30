from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import growth, mega_drain


card = PokemonCardDef(
    guid="f500168b-179d-5585-9b73-066f57cfe3b3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic", "Sunkern"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=191,
    abilities=[
        Attack(
            title="Growth",
            game_text="Flip a coin. If heads, you may attach up to 2 Grass Energy cards from your hand to Sunkern.",
            cost={PokemonTypes.GRASS: 1},
            effect=growth,
        ),
        Attack(
            title="Mega Drain",
            game_text="Remove a number of damage counters from Sunkern equal to half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Sunkern has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=mega_drain,
        ),
    ],
)
