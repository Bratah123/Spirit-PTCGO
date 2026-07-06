from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="509d2a69-ecab-5d21-aba8-ed46f8063d2e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Nadir Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned. During Pok\u00e9mon Checkup, put 8 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)