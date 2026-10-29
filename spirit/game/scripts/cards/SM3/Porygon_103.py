from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import code_check

card = PokemonCardDef(
    guid="bc5a7d8c-1f6c-5d49-9c4b-1684733dc165",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Code Check",
            game_text="Look at 1 of your opponent's face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=code_check,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
