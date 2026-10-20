from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="7d253950-918d-57ad-a26d-7c67d77132d5",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic", "Vullaby"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=629,
    abilities=[
        Attack(
            title="Rear Guard",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
