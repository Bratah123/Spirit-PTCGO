from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="6136860c-84ef-5070-8585-568119f4ad2a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=104,
    abilities=[
        Attack(
            title="Teary Eyes",
            game_text="During your opponent's next turn, any damage done to Cubone by attacks is reduced by 20.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
