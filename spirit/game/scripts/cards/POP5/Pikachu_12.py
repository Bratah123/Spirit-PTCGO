from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import thunderbolt_discard_all


card = PokemonCardDef(
    guid="fe253141-5da9-58ae-b97e-34e7eff8fb8e",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="POP5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Pikachu.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=thunderbolt_discard_all(50),
        ),
    ],
)
