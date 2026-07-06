from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd92eed4-3c14-57e5-87db-240e7ac442f7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic", "Wooloo"],
    subtypes=["Basic"],
    collector_number=221,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Derail",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Let's All Rollout",
            game_text="This attack does 20 damage for each of your Benched Pok\u00e9mon that has the Let's All Rollout attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)