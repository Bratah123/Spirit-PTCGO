from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import thundersquall


card = PokemonCardDef(
    guid="40a27a7a-bd70-56ce-b583-9ebd34ee2476",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningRaichu.Name",
    display_name="Shining Raichu",
    searchable_by=["Shining Raichu", "Basic", "ShiningRaichu"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=26,
    abilities=[
        Attack(
            title="Thundersquall",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to that Pok\u00e9mon for each Water Energy attached to Shining Raichu. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.WATER: 2},
            damage=40,
            effect=thundersquall,
        ),
    ],
)
