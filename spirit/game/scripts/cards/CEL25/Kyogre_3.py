from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6921130-84f9-5a4b-b273-47fba72812f9",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Aqua Storm",
            game_text="Discard the top 5 cards of your deck, and then choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 50 damage for each Energy card you discarded in this way to each of those Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)