from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4a569ea-e41b-5229-8588-ae1f7ffd1c17",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=203,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Expert in Roundness",
            game_text="Prevent all damage done to each of your Pok\u00e9mon that has the Let's All Rollout attack by attacks from your opponent's Pok\u00e9mon VMAX.",
            effect=unimplemented,
        ),
        Attack(
            title="Let's All Rollout",
            game_text="This attack does 20 damage for each of your Benched Pok\u00e9mon that has the Let's All Rollout attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)