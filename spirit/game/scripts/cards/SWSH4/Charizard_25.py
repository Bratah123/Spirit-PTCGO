from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5b1a323-c6ec-5e9b-8867-be373de5a922",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Battle Sense",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and put 1 of them into your hand. Discard the other cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Royal Blaze",
            game_text="This attack does 50 more damage for each Leon card in your discard pile.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)