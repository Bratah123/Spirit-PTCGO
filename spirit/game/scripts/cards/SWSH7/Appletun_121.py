from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ade82de6-2bc0-5531-bc7a-3ebc2dbd264c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Thick Mucus",
            game_text="This attack does 70 damage for each Special Energy card attached to your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Fighting Tackle",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)