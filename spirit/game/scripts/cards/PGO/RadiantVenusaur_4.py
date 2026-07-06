from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2baf28dd-fef2-52c9-826b-1fbf5017d922",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantVenusaur.Name",
    display_name="Radiant Venusaur",
    searchable_by=["Radiant Venusaur", "Basic", "Radiant", "RadiantVenusaur"],
    subtypes=["Basic", "Radiant"],
    collector_number=4,
    set_code="PGO",
    rarity=Rarities.RareRadiant,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Ability(
            title="Sunny Bloom",
            game_text="Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 4 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Pollen Hazard",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)