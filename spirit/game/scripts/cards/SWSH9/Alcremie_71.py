from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37d5a9ae-c2a9-5bc2-9ba0-da81317e2bca",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Ability(
            title="Additional Order",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your turn does not end when you use Caf\u00e9 Master.",
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Flavor",
            game_text="This attack does 40 more damage for each type of basic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)