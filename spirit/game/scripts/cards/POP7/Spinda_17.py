from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dish_out_top_and_bottom, synchro_punch

card = PokemonCardDef(
    guid="8c089fcb-8650-5d0d-8879-f22b9c4a8e82",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=['Spinda', 'Basic', 'Spinda'],
    subtypes=["Basic"],
    collector_number=17,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="Dish Out",
            game_text="Draw a card from the top and the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dish_out_top_and_bottom(),
        ),
        Attack(
            title="Synchro Punch",
            game_text="If any basic Energy card attached to Spinda is the same type as any Energy attached to the Defending Pokémon, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=synchro_punch(10, 30),
        ),
    ],
)
