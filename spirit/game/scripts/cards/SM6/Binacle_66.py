from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="74d6152a-6ad9-58a3-84fe-b52eb69da57c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    display_name="Binacle",
    searchable_by=["Binacle", "Basic", "Binacle"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=688,
    abilities=[
        Attack(
            title="Allotment",
            game_text="Draw a card.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=draw_attack(1),
        ),
    ],
)
