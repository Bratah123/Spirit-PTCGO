from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import wink_wink

card = PokemonCardDef(
    guid="ad79583a-5eba-58e7-a41c-c366da380852",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1", "Sylveon"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=700,
    abilities=[
        Attack(
            title="Wink Wink",
            game_text="Your opponent reveals their hand. You may discard a Supporter card you find there and use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wink_wink,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
