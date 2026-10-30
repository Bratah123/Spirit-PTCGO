from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import plasma_attach

card = PokemonCardDef(
    guid="5a04d25d-81d9-5972-ae0c-f59495bab2ff",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Plasma",
            game_text="Flip a coin. If heads, search your discard pile for a Lightning Energy card and attach it to Pikachu.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=plasma_attach(),
        ),
    ],
)